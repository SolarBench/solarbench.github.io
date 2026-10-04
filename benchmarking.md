---
title: Benchmarking
layout: home
nav_order: 1
parent: Use Cases
---

<link rel="stylesheet" href="{{ '/assets/css/use-case-tables.css' | relative_url }}?v={{ site.time | date: '%s' }}">

# Standardized Cross-site Benchmarking

SolarBench's multi-continental datasets and Python toolbox enable consistent comparison of solar nowcasting methods across diverse locations and forecasting conditions within a standardized framework. We describe below the standardized nowcasting tasks, comprehensive evaluation metrics, and representative models used for benchmarking.

## Standardized nowcasting tasks

SolarBench defines standardized tasks for predicting solar irradiance or PV output using consistent input-output configurations and forecast horizons. The table below summarizes the benchmark configuration. The toolbox further standardizes data loading, temporal alignment, sample construction, train–test splits, model training, and evaluation to support reproducible cross-site benchmarking.

<div class="use-case-table benchmark-configuration-table" markdown="1">

| Component | Configuration |
|---|---|
| Prediction targets | Irradiance or PV output |
| Input modalities | One or more of historical measurements, sky imagery, and satellite imagery |
| Lead times | 10, 30, 60, 90, 120 min |
| Historical input window | 15 min [4 time steps,  *t-15* to *t* with 5-min interval]* |
| Historical input resolution | 5 min** |
| Target aggregation | Forward 5-min average |
| Historical measurement aggregation | Backward 5-min average |

</div>

<div class="benchmark-table-notes" markdown="1">

*\* For models combining sky and satellite imagery, the same number of input time steps (i.e., 4) is used for each modality. Because satellite imagery may have a coarser cadence (e.g., 10 min), its effective historical window can be longer than 15 min.*

*\*\* Ground-based data use 5-min resolution; satellite inputs use their native temporal resolution.*

</div>

## Evaluation metrics

SolarBench includes a range of evaluation metrics for assessing solar nowcasting performance. Here, we highlight two complementary metrics: **forecast skill** for level prediction and **ramp recall** for rapid-change prediction. Additional metrics including RMSE, rRMSE, MAE, MBE, and temporal distortion mix (TDM), are also implemented in the SolarBench toolbox.

### Level prediction

Level prediction measures overall accuracy in estimating future irradiance or PV output. Forecast skill is defined as the improvement in RMSE related to persistence:

<div class="benchmark-equation" role="math" aria-label="Forecast skill equals one minus RMSE divided by reference RMSE, multiplied by 100 percent">
  <span>Forecast skill = (1 − </span><span class="benchmark-fraction"><span>RMSE</span><span>RMSE<sub>ref</sub></span></span><span>) × 100%</span>
</div>

Positive values indicate improvement over the persistence baseline, while negative values indicate poorer performance.

### Ramp prediction

Ramp prediction evaluates whether models capture rapid changes in irradiance or PV output caused by evolving cloud conditions. SolarBench introduces an event-based **ramp recall** metric that assesses whether predicted ramps reproduce observed events in occurrence, direction, and magnitude within a specified relative error tolerance.

<div class="benchmark-equation" role="math" aria-label="Ramp recall equals correctly predicted ramp events divided by observed ramp events, multiplied by 100 percent">
  <span>Ramp recall = </span><span class="benchmark-fraction"><span>Correctly predicted ramp events</span><span>Observed ramp events</span></span><span> × 100%</span>
</div>

For this benchmarking demonstration, ramp events are identified using a clear sky index change threshold of 0.1, with a 30% relative ramp-magnitude error tolerance.

## Benchmarking models

We benchmark five representative solar irradiance nowcasting models as a demonstration. The models span commonly used baselines and image-based deep learning architectures.

<div class="use-case-table benchmark-model-table" markdown="1">

| Model | Architecture | Input modalities |
|---|---|---|
| Persistence | Smart persistence | Current irradiance value |
| MLP [1] | Multilayer perceptron | Historical irradiance sequence |
| SUNSET [2] | Convolutional neural network | Sky images + irradiance sequence |
| OmniVision [3] | Multimodal CNN | Sky images + satellite images + irradiance sequence |
| ViT [4, 5] | Vision Transformer with temporal attention | Sky images + irradiance sequence |

</div>

SolarBench also includes ground-based meteorological measurements, weather forecasts, and reanalysis data to support future development of additional multimodal forecasting approaches.

**Model references**

1. Pedro, H. T., and Coimbra, C. F. (2012). Assessment of forecasting techniques for solar power production with no exogenous inputs. *Solar Energy*, 86(7), 2017–2028.
2. Sun, Y., Venugopal, V., and Brandt, A. R. (2019). Short-term solar power forecast with deep learning: Exploring optimal input and output configuration. *Solar Energy*, 188, 730–741.
3. Paletta, Q., Arbod, G., and Lasenby, J. (2023). OmniVision forecasting: Combining satellite and sky images for improved deterministic and probabilistic intra-hour solar energy predictions. *Applied Energy*, 336, 120818.
4. Zhang, L., Wilson, R., Sumner, M., and Wu, Y. (2023). Advanced multimodal fusion method for very short-term solar irradiance forecasting using sky images and meteorological data: A gate and transformer mechanism approach. *Renewable Energy*, 216, 118952.
5. Bertasius, G., Wang, H., and Torresani, L. (2021). Is space-time attention all you need for video understanding? In *ICML*, vol. 2, p. 4.

## Key findings

Our experiments reveal an important gap between average forecasting accuracy and the ability to capture rapid solar fluctuations.

**Image-based deep learning improves overall accuracy.** Across sites and lead times, SUNSET, OmniVision, and ViT achieve approximately 10–20% median forecast skill over persistence. Differences among these advanced architectures remain relatively modest, generally within 3–6 percentage points.

**Rapid solar fluctuations remain difficult to predict.** Despite improved aggregate accuracy, deep learning models often capture fewer than 5% of observed ramp events under a 30% relative error tolerance. Under highly variable conditions, smoother forecasts can reduce overall error while missing rapid irradiance transitions.

**Performance varies across forecasting environments.** No single model consistently dominates across all locations, lead times, and evaluation objectives. Persistence remains competitive under stable conditions and can exhibit higher ramp recall despite larger level prediction errors.

These findings highlight the importance of evaluating forecasting methods across diverse environments and multiple performance dimensions, rather than relying on single-site results or aggregate accuracy alone.

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_benchmark_performance.jpg' | relative_url }}" alt="Benchmark results showing aggregate forecast skill and ramp recall, example irradiance forecasts, and site-level model performance." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Benchmarking of level and ramp prediction performance across lead times and locations. a</strong>, Aggregated forecasting performance. (i) Level prediction performance quantified by forecast skill (%), defined as the improvement in RMSE related to persistence (i.e., persistence has a forecast skill of zero). Solid lines denote the median across locations, and shaded bands denote the interquartile range. (ii) Ramp recall, defined as the fraction of observed ramp events successfully captured within a 30% relative error threshold, aggregated across sites in the same manner. <strong>b</strong>, Example irradiance forecasts from representative models at a 60 min lead time under relatively stable and highly variable conditions. The stable case highlights the competitiveness of persistence under limited variability, whereas the highly variable case shows that image-based deep learning models achieve better level prediction accuracy but produce smoother forecasts that miss many rapid irradiance transitions, revealing a gap between aggregate accuracy and ramp event detection. Observed and successfully predicted ramp events are highlighted. <strong>c</strong>, Site-level forecasting performance. (i) Best-performing model at each site and lead time for forecast skill and ramp recall. Each circle represents a site–lead time pair, and marker color denotes the best-performing model. (ii), Irradiance forecasting RMSE of the ViT model across sites and lead times. Locations are sorted by RMSE at the 10 min lead time.
</em></figcaption>
</figure>
