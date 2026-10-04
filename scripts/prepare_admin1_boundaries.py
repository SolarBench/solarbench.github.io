"""Create compact map-ready Natural Earth state/province boundary lines.

Download ne_10m_admin_1_states_provinces_lines.zip into
_local/map-label-sources/ before running this script.
"""

import json
from pathlib import Path

import pyogrio


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "_local/map-label-sources/ne_10m_admin_1_states_provinces_lines.zip"
OUTPUT = ROOT / "assets/data/natural_earth/admin1-boundaries.geojson"


def rounded_line(line):
    return [[round(x, 4), round(y, 4)] for x, y in line.coords]


def main():
    data = pyogrio.read_dataframe(SOURCE, columns=["MIN_ZOOM"])
    groups = {"overview": [], "regional": [], "detail": []}
    for min_zoom, geometry in zip(data.MIN_ZOOM, data.geometry):
        if geometry is None or min_zoom > 8:
            continue
        group = "overview" if min_zoom <= 5 else "regional" if min_zoom <= 7 else "detail"
        geometry = geometry.simplify(0.025, preserve_topology=False)
        parts = [geometry] if geometry.geom_type == "LineString" else geometry.geoms
        for part in parts:
            line = rounded_line(part)
            if len(line) >= 2:
                groups[group].append(line)

    features = [
        {"type": "Feature", "properties": {"level": level},
         "geometry": {"type": "MultiLineString", "coordinates": lines}}
        for level, lines in groups.items()
    ]
    OUTPUT.write_text(json.dumps({"type": "FeatureCollection", "features": features}, separators=(",", ":")))
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {OUTPUT.stat().st_size:,} bytes")
    print({level: len(lines) for level, lines in groups.items()})


if __name__ == "__main__":
    main()
