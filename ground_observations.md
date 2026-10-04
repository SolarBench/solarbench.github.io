---
title: Ground-based Observations
layout: home
nav_order: 1
parent: Datasets
---

## Ground-based Observations
Ground-based data are collected from both open-source datasets and previously unreleased collections contributed by research groups as part of this collaborative initiative. For open-source datasets, we provide links to the relevant publications or repositories for more details. For newly released datasets, descriptions are provided within this document. Each dataset follows its own license, and users should adhere to the specific licensing terms when using the data.

Ground-based observations include sky images, meteorological measurements, and PV output where available. Meteorological measurements include various irradiance components, such as global horizontal irradiance (GHI), direct normal irradiance (DNI), diffuse horizontal irradiance (DHI), and global tilt irradiance (GTI), as well as air temperature, relative humidity, pressure, wind speed, and wind direction. Among these variables, solar irradiance and PV output serve as the primary prediction target for solar forecasting tasks. The table below provides details for each ground-based dataset.

<table id="solarbench-table" class="display nowrap solarbench-table" style="width:100%">
  <thead>
    <tr>
      <th>Site</th>
      <th>Data Source</th>
      <th>Frequency (min)</th>
      <th>Data Size (GB)</th>
      <th>Number of Samples </th>
      <th>Split (Train:Test)</th>
      <th>Data Included</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Puy de Dôme, France</td>
      <td><a href="https://amt.copernicus.org/articles/13/3413/2020/amt-13-3413-2020.html" target="_blank" rel="noopener">CO-PDD</a></td>
      <td>1, 2<sup>**</sup><br></td>
      <td>7.4</td>
      <td>981,409</td>
      <td>93%:7%</td>
      <td>Time Stamp, Sky image, GHI, DNI, DHI, Air temperature, Relative humidity, Pressure, Wind speed, Wind direction, Precipitation, Irradiance_IR</td>
    </tr>

    <tr>
      <td>Akwatia, Ghana</td>
      <td>EnerSHelF-Akwatia</td>
      <td>1</td>
      <td>0.6</td>
      <td>89,953</td>
      <td>94%:6%</td>
      <td>Time Stamp, Sky image, GTI</td>
    </tr>

    <tr>
      <td>Kologo, Ghana</td>
      <td>EnerSHelF-Kologo</td>
      <td>1</td>
      <td>0.7</td>
      <td>92,182</td>
      <td>94%:6%</td>
      <td>Time Stamp, Sky image, GTI</td>
    </tr>

    <tr>
      <td>Sankt Augustin, Germany</td>
      <td>EnerSHelF-StAugustin</td>
      <td>1</td>
      <td>3.3</td>
      <td>442,788</td>
      <td>95%:5%</td>
      <td>Time Stamp, Sky image, GHI, GHI_pyr, DNI, DHI</td>
    </tr>

    <tr>
      <td>Hong Kong, China</td>
      <td>HKPolyUSky</td>
      <td>1</td>
      <td>1.5</td>
      <td>223,812</td>
      <td>95%:5%</td>
      <td>Time Stamp, Sky image, GHI, DHI, Air temperature, Relative humidity, Pressure, Wind speed, Wind direction</td>
    </tr>

    <tr>
      <td>Paris, France</td>
      <td><a href="https://sirta.ipsl.polytechnique.fr/index.html" target="_blank" rel="noopener">SIRTA</a></td>
      <td>1, 2<sup>*</sup></td>
      <td>10.5</td>
      <td>1,368,060</td>
      <td>95%:5%</td>
      <td>Time Stamp, Sky image, GHI, GHI_std, GHI_min, GHI_max, DNI, DNI_std, DNI_min, DNI_max, DHI, DHI_std, DHI_min, DHI_max, LWd_max, Air temperature, Relative humidity, Pressure</td>
    </tr>

    <tr>
      <td>Stanford, USA</td>
      <td><a href="https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset" target="_blank" rel="noopener">SKIPPD</a></td>
      <td>1</td>
      <td>2.3</td>
      <td>363,375</td>
      <td>96%:4%</td>
      <td>Time stamp, Sky image, PV output</td>
    </tr>

    <tr>
      <td>Golden, USA</td>
      <td><a href="https://midcdmz.nrel.gov/apps/sitehome.pl?site=BMS" target="_blank" rel="noopener">SRRL-BMS</a></td>
      <td>1</td>
      <td>2.9</td>
      <td>367,878</td>
      <td>94%:6%</td>
      <td>Time Stamp, Sky image, GHI, DNI, DHI, Air temperature, Relative humidity, Pressure, Wind speed, Wind direction, Max wind speed, Precipitation</td>
    </tr>

    <tr>
      <td>Folsom, USA</td>
      <td><a href="https://zenodo.org/records/2826939" target="_blank" rel="noopener">
   UCSD-Folsom</a></td>
      <td>1</td>
      <td>5.9</td>
      <td>765,140</td>
      <td>94%:6%</td>
      <td>Time Stamp, Sky image, GHI, DNI, DHI, Air temperature, Relative humidity, Pressure, Wind speed, Wind direction, Max wind speed, Precipitation</td>
    </tr>

    <tr>
      <td>Nottingham, UK</td>
      <td>UNottingham</td>
      <td>1</td>
      <td>0.5</td>
      <td>68,237</td>
      <td>89%:11%</td>
      <td>Time Stamp, Sky image, GHI, DNI, DHI, GHI_min_avg, DNI_min_avg, DHI_min_avg, Clear-sky GHI, Clear-sky DNI, Clear-sky DHI, Air temperature, Relative humidity, Pressure, Wind speed, Wind direction, Solar zenith angle, Solar azimuth angle</td>
    </tr>

    <tr>
      <td>Gatton, Australia</td>
      <td><a href="https://espace.library.uq.edu.au/view/UQ:bd7e108" target="_blank" rel="noopener">UQueensland</a></td>
      <td>1</td>
      <td>0.4</td>
      <td>69,347</td>
      <td>94%:6%</td>
      <td>Time Stamp, Sky image, PV output</td>
    </tr>

  </tbody>
</table>
<p class="table-footnote" style="font-size: 0.78rem;" >* SIRTA data frequency: 2015-2017: 1 min; 2018-2022: 2 min<br>
** CO-PDD data frequencey: 2015.12-2018.09: 1 min; 2018.10-2023.08: 2 min</p>

<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>

<script>
$('#solarbench-table').DataTable({
    scrollY: false,
    scrollX: true,
    scrollCollapse: true,
    paging: false,
    searching: false,
    info: false,
    autoWidth: false
});
</script>
