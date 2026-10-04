"""Render the supplied historical GeoTIFF without blending climate classes.
Requires rasterio, numpy and Pillow. Missing grid cells remain transparent.
"""
import csv
import json
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
COLORS = {
'Af':(16,1,242,255),'Am':(52,113,243,255),'As':(84,152,223,255),'Aw':(124,175,224,255),
'BWh':(255,0,0,255),'BWk':(255,150,150,255),'BSh':(245,165,0,255),'BSk':(255,220,100,255),
'Csa':(255,255,0,255),'Csb':(200,200,0,255),'Csc':(150,150,0,255),
'Cwa':(150,255,150,255),'Cwb':(100,200,100,255),'Cwc':(50,150,50,255),
'Cfa':(200,255,80,255),'Cfb':(100,255,80,255),'Cfc':(50,200,0,255),
'Dsa':(255,0,255,255),'Dsb':(200,0,200,255),'Dsc':(150,50,150,255),'Dsd':(150,100,150,255),
'Dwa':(170,175,255,255),'Dwb':(90,120,220,255),'Dwc':(75,80,180,255),'Dwd':(50,0,135,255),
'Dfa':(0,255,255,255),'Dfb':(55,200,255,255),'Dfc':(0,125,125,255),'Dfd':(0,70,95,255),
'ET':(128,128,128,255*.3),'EF':(128,128,128,255*.6)}
# Use the latest historical period, not a future scenario.
import re
import zipfile
import rasterio
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_bounds

archive = ROOT / 'assets/data/koppen_geiger_tif.zip'
member = '1991_2020/koppen_geiger_0p00833333.tif'
with zipfile.ZipFile(str(archive)) as z:
    source_legend = z.read('legend.txt').decode('utf-8')
classes = [(int(n), code, description.strip()) for n, code, description in
           re.findall(r'^\s*(\d+):\s+(\w+)\s+(.+?)\s+\[', source_legend, re.M)]
assert len(classes) == 30
size = 2880
limit = 20037508.342789244
transform = from_bounds(-limit, -limit, limit, limit, size, size)
result = np.zeros((size, size), dtype=np.uint8)
with rasterio.open('/vsizip/' + str(archive) + '/' + member) as src:
    print('Source:', src.crs, src.shape, src.res, 'nodata:', src.nodata)
    assert src.count == 1 and src.crs.to_epsg() == 4326
    reproject(source=rasterio.band(src, 1), destination=result,
              src_transform=src.transform, src_crs=src.crs, src_nodata=src.nodata,
              dst_transform=transform, dst_crs='EPSG:3857', dst_nodata=0,
              resampling=Resampling.nearest)
    resolution = src.res[0]
assert set(np.unique(result)).issubset({0} | {n for n, _, _ in classes})
palette = np.zeros((256, 4), dtype=np.uint8)
for n, code, _ in classes:
    palette[n] = [round(v) for v in COLORS[code]]
rgba = palette[result]
out = ROOT / 'assets/data/koppen'
out.mkdir(exist_ok=True)
Image.fromarray(rgba, 'RGBA').save(str(out / 'koppen-mercator.png'), optimize=True)
legend = [{'code': code, 'description': description, 'rgba': list(COLORS[code]),
           'css': 'rgba(%s, %s, %s, %s)' % (*COLORS[code][:3], COLORS[code][3]/255)}
          for _, code, description in classes]
(ROOT / '_data/koppen_legend.json').write_text(json.dumps(legend, indent=2)+'\n')
metadata = {'source_file': 'assets/data/koppen_geiger_tif.zip', 'archive_member': member,
            'period': '1991–2020', 'resolution_degrees': resolution,
            'display_size_pixels': [size, size], 'projection': 'EPSG:3857',
            'resampling': 'nearest neighbor', 'missing_cells': 'transparent',
            'source_attribution': 'Beck et al. (2023), Scientific Data 10, 724',
            'classes': len(classes), 'palette': 'User-supplied colors; As omitted because absent from source'}
(out / 'metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
(out / 'SOURCE.txt').write_text(source_legend)
print('Rendered latest historical climate map with 30 classes.')
