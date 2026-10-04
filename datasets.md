---
title: Datasets
layout: home
nav_order: 4
has_children: false
---

<div class="datasets-heading">
  <h1>Datasets</h1>
  <div class="datasets-actions">
    <a href="https://huggingface.co/solarbench" class="btn btn-primary" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">🤗</span> Browse datasets on Hugging Face</a>
    <a href="{{ "/contribution.html" | relative_url }}" class="btn">Contribute a dataset</a>
  </div>
</div>

SolarBench harmonizes multimodal observations from 11 sites across five continents and seven countries, spanning diverse climate, solar resource, and short-term variability regimes. This diversity enables systematic evaluation of model robustness across diverse forecasting environments. Each site includes three complementary categories of data:

<div class="modality-table" markdown="1">

|  | What it includes | Information provided | Data source |
| --- | --- | --- | --- |
| **Ground-based observations** | Sky images, meteorological measurements, and solar irradiance or PV output | Local cloud and weather conditions; Irradiance or PV output as prediction targets | Open datasets & New contributions |
| **Remote sensing imagery** | Geostationary satellite imagery from GOES, Himawari, and Meteosat Second Generation (MSG) | Regional cloud patterns and evolution | Open archives |
| **Atmospheric model products** | ECMWF Reanalysis v5 (ERA5) and numerical weather prediction (NWP) from NOAA’s Global Forecast System (GFS) | Forecast and historical atmospheric conditions | Open archives |

*Note: Check [Citation](citation.html) for references to individual data sources.*

</div>


## Explore the datasets
Explore the interactive map to learn about SolarBench sites and their characteristics, and compare key attributes across sites below.

<link rel="stylesheet" href="{{ '/assets/css/dataset-workspace.css' | relative_url }}?v={{ site.time | date: '%s' }}">

<div class="dataset-workspace">
  {% include solarbench-map.html %}
  {% include site-comparison.html %}
</div>
{% include solarbench-map.js.html %}
<!--
<style>
#solarbench-spatiotemporal-charac th,
#solarbench-spatiotemporal-charac td {
  white-space: nowrap;
}
</style>

<div style="width:100%; overflow:hidden;">
<table id="solarbench-spatiotemporal-charac" class="display" style="width:1400px">
  <thead>
    <tr>
      <th>Site</th>
      <th>Country</th>
      <th>Continent</th>
      <th>Latitude, Longitude (°)</th>
      <th>Köppen-Geiger Climate Type</th>
      <th>Start Date</th>
      <th>End Date</th>
      <th>Duration (years)</th>
      <th>Data</th>
    </tr>
  </thead>
  <tbody>
    {% for location in site.data.sites %}
    <tr>
      <td>{{ location.site_name | escape }}</td>
      <td>{{ location.country | escape }}</td>
      <td>{{ location.continent | escape }}</td>
      <td>{{ location.lat | round: 3 }}, {{ location.lon | round: 3 }}</td>
      <td>{{ location.climate.koppen_geiger | escape }}</td>
      <td>{{ location.start_date }}</td>
      <td>{{ location.end_date }}</td>
      <td>{{ location.duration_years }}</td>
      <td>{{ location.data | join: ', ' | escape }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/fixedcolumns/4.3.0/css/fixedColumns.dataTables.min.css">
<script src="https://cdn.datatables.net/fixedcolumns/4.3.0/js/dataTables.fixedColumns.min.js"></script>

<script>
$(document).ready(function () {
  $('#solarbench-spatiotemporal-charac').DataTable({
    scrollX: true,
    scrollCollapse: true,
    paging: false,
    searching: false,
    info: false,
    autoWidth: false,
    fixedColumns: {
      left: 1
    }
  });
});
</script>
-->
