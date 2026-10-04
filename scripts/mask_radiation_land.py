"""Make the solar-radiation image transparent outside Natural Earth land areas."""

import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_bounds
from rasterio.warp import transform_geom


ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / "assets/data/solar_radiation/ssrd-mercator.png"
COUNTRIES = ROOT / "assets/data/natural_earth/countries.geojson"


def apply_land_mask(image_path=IMAGE, countries_path=COUNTRIES):
    image_path = Path(image_path)
    countries = json.loads(Path(countries_path).read_text())
    with rasterio.open(image_path) as source:
        rgba = source.read()
        height, width = source.height, source.width
    if rgba.shape[0] != 4 or height != width:
        raise ValueError("Expected a square RGBA Web Mercator image")

    # Oversample coastlines to retain partially covered edge pixels.
    scale = 2
    half_world = 6378137 * np.pi
    transform = from_bounds(
        -half_world, -half_world, half_world, half_world,
        width * scale, height * scale,
    )
    geometries = (
        (transform_geom("EPSG:4326", "EPSG:3857", feature["geometry"]), 1)
        for feature in countries["features"]
    )
    land = rasterize(
        geometries,
        out_shape=(height * scale, width * scale),
        transform=transform,
        dtype="uint8",
    )
    coverage = land.reshape(height, scale, width, scale).sum(axis=(1, 3))
    land_alpha = np.rint(coverage * (255 / (scale * scale))).astype("uint8")
    rgba[3] = np.minimum(rgba[3], land_alpha)

    with TemporaryDirectory(dir=image_path.parent) as temporary:
        output = Path(temporary) / image_path.name
        with rasterio.open(output, "w", driver="PNG", width=width, height=height,
                           count=4, dtype="uint8") as target:
            target.write(rgba)
        os.replace(output, image_path)


if __name__ == "__main__":
    apply_land_mask()
    print(f"Masked oceans in {IMAGE}")
