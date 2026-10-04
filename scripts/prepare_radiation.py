"""Prepare a Web Mercator image from the supplied regular global SSRD grid.

Requires h5py, numpy, scipy, matplotlib, Pillow, rasterio. Values are used as supplied;
no unit conversion or temporal averaging is performed.
"""
from pathlib import Path
import json
import h5py
import numpy as np
from scipy.ndimage import map_coordinates
from matplotlib import cm
from PIL import Image
from mask_radiation_land import apply_land_mask

root = Path(__file__).resolve().parents[1]
with h5py.File(str(root / 'assets/data/ssrd.nc'), 'r') as f:
    lat = f['latitude'][:]
    lon = f['longitude'][:]
    data = f['ssrd'][:]
assert data.shape == (len(lat), len(lon))
assert np.allclose(np.diff(lat), -0.25) and np.allclose(np.diff(lon), 0.25)
assert lat[0] == 90 and lon[0] == 0
# Uniform projected pixel centers, clipped at the Web Mercator latitude limit.
# Reprojection is required: a geographic image would misalign with the Web Mercator map.
size = 1440
xs = (np.arange(size) + 0.5) / size
ys = (np.arange(size) + 0.5) / size
latitude = np.degrees(np.arctan(np.sinh(np.pi * (1 - 2 * ys))))
longitude = xs * 360 - 180
rows = (90 - latitude) / 0.25
cols = (longitude % 360) / 0.25
# Extend the cyclic longitude seam for bilinear interpolation.
wrapped = np.concatenate([data, data[:, :1]], axis=1)
r, c = np.meshgrid(rows, cols, indexing='ij')
values = map_coordinates(wrapped, [r, c], order=1, mode='nearest')
bounds = np.arange(50, 326, 25)
palette = (cm.get_cmap('OrRd', len(bounds)-1)(np.arange(len(bounds)-1)) * 255).astype('uint8')
indices = np.clip(np.searchsorted(bounds, values, side='right') - 1, 0, len(palette)-1)
rgba = palette[indices]
legend = [{'lower': int(bounds[i]), 'upper': int(bounds[i+1]), 'color': '#%02x%02x%02x' % tuple(color[:3])} for i, color in enumerate(palette)]
(root / '_data/radiation_legend.json').write_text(json.dumps(legend, indent=2)+'\n')
rgba[~np.isfinite(values), 3] = 0
out = root / 'assets/data/solar_radiation'
Image.fromarray(rgba, 'RGBA').save(str(out / 'ssrd-mercator.png'), optimize=True)
apply_land_mask(out / 'ssrd-mercator.png')
meta = {'source_file':'assets/data/ssrd.nc', 'projection':'EPSG:3857',
        'coordinates':[[-180,85.05112878],[180,85.05112878],[180,-85.05112878],[-180,-85.05112878]],
        'color_range':[50,325], 'color_boundaries':bounds.tolist(), 'colormap':'OrRd', 'units':'W/m²',
        'averaging_period':'1980–2020', 'source':'ERA5',
        'land_mask':'Natural Earth 1:50m countries',
        'native_range':[float(np.nanmin(data)),float(np.nanmax(data))]}
(out / 'metadata.json').write_text(json.dumps(meta, indent=2)+'\n')
print('Prepared radiation image; ERA5 1980–2020, W/m² (confirmed by data provider).')
