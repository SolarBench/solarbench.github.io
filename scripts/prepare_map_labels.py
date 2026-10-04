"""Build compact map labels from locally downloaded Natural Earth shapefiles."""

import json
from pathlib import Path

import pyogrio
from shapely.geometry import Point


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "_local" / "map-label-sources"
OUTPUT = ROOT / "assets" / "data" / "natural_earth" / "labels.json"


def source(name, columns):
    return pyogrio.read_dataframe(f"zip://{SOURCES / (name + '.zip')}", columns=columns)


def label(name, point, rank):
    return {"name": name, "lat": round(point.y, 4), "lon": round(point.x, 4), "rank": int(rank)}


def build_labels():
    countries = source("ne_50m_admin_0_countries", ["NAME", "LABEL_X", "LABEL_Y", "LABELRANK"])
    country_labels = []
    for row in countries.itertuples():
        if row.NAME and row.LABEL_X is not None and row.LABEL_Y is not None:
            country_labels.append({
                "name": row.NAME,
                "lat": round(float(row.LABEL_Y), 4),
                "lon": round(float(row.LABEL_X), 4),
                "rank": int(row.LABELRANK),
            })

    regions = source("ne_10m_admin_1_states_provinces", ["name", "admin", "labelrank"])
    largest_regions = {}
    for row in regions.itertuples():
        if not row.name or row.geometry is None or row.geometry.is_empty or row.labelrank is None:
            continue
        geometry = row.geometry
        main_area = max(geometry.geoms, key=lambda part: part.area) if geometry.geom_type == "MultiPolygon" else geometry
        key = (row.admin, row.name)
        if key not in largest_regions or main_area.area > largest_regions[key][0]:
            largest_regions[key] = (main_area.area, label(row.name, main_area.representative_point(), row.labelrank))
    region_labels = [item[1] for item in largest_regions.values()]
    site_regions = {}
    for site in json.loads((ROOT / "_data" / "sites.json").read_text()):
        matches = regions[regions.geometry.covers(Point(site["lon"], site["lat"]))]
        if not matches.empty:
            site_regions[site["id"]] = matches.iloc[0]["name"]

    places = source("ne_50m_populated_places", ["NAME", "SCALERANK"])
    place_labels = [label(row.NAME, row.geometry, row.SCALERANK) for row in places.itertuples()
                    if row.NAME and row.geometry is not None and not row.geometry.is_empty]

    for entries in (country_labels, region_labels, place_labels):
        entries.sort(key=lambda entry: (entry["rank"], entry["name"]))
    OUTPUT.write_text(json.dumps({"countries": country_labels, "regions": region_labels, "places": place_labels,
                                  "siteRegions": site_regions},
                                 ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Wrote {len(country_labels)} country, {len(region_labels)} region, and {len(place_labels)} place labels")


if __name__ == "__main__":
    build_labels()
