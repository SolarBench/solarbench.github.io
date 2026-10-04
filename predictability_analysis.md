---
title: Predictability Analysis
layout: home
nav_order: 1
parent: Use Cases
---

<link rel="stylesheet" href="{{ '/assets/css/use-case-tables.css' | relative_url }}?v={{ site.time | date: '%s' }}">


# Solar Predictability Analysis

Understanding what governs forecasting difficulty, or predictability, is critical to improving solar nowcasting methods. Predictability can also inform solar site selection, as locations with similar solar resource potential may differ in how reliably their output can be forecast.

SolarBench enables systematic analysis of predictability across geographically distributed sites, diverse atmospheric conditions, and forecast horizons. We demonstrate this capability by examining two complementary questions:

- How can we quantify and compare forecasting difficulty across sites?
- How do different cloud regimes influence solar predictability?

## Quantifying site-level predictability

### Variability ≠ Predictability

We examine whether the variability index, a commonly used measure of fluctuations in solar resources (see equation below), provides a useful indicator of forecasting difficulty. Its relationship with forecasting error is weak and inconsistent across sites and lead times. Therefore, variability alone is not a reliable indicator of predictability.

<div class="benchmark-equation">
  <img src="{{ '/assets/imgs/variability-index-equation.svg' | relative_url }}?v=3" alt="Variability index at delta t equals the square root of the mean of squared clear sky index changes over delta t-minute intervals." style="display: block; width: 100%; max-width: 340px; height: auto; margin: 0 auto;">
</div>

Here, <i>k</i><sub>cs</sub> is the clear sky index and <i>N</i> and we use Δt = 5 min in this study.

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_VI_vs_error.jpg' | relative_url }}" alt="Forecasting rRMSE versus variability index for MLP, OmniVision, and ViT at 10-, 60-, and 120-minute lead times, with site points, fitted lines, and correlation coefficients." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Relationship between forecasting error and the variability index.</strong> rRMSE of the MLP, OmniVision, and ViT models is plotted against the variability index for the 10-, 60-, and 120-min lead times. Each point represents one SolarBench site, and solid lines indicate least-squares linear fits. Pearson correlation coefficients between rRMSE and the variability index are reported for each model. </em></figcaption>
</figure>

### Persistence error as a predictability indicator

Persistence assumes that the current clear sky index remains constant over the forecast horizon. We use the relative root mean square error (rRMSE) of the persistence model as a proxy for forecasting difficulty. We find that persistence rRMSE shows strong and consistent correlations with deep learning forecasting errors, with Pearson correlation coefficients typically exceeding 0.85. It provides a simple, readily computed indicator of relative forecasting difficulty across diverse environments.

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_persistence_rrmse_vs_error.jpg' | relative_url }}" alt="Forecasting error versus persistence rRMSE across sites for MLP, OmniVision, and ViT at 10-, 60-, and 120-minute lead times, with Pearson correlation coefficients." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Relationship between forecasting error and persistence error.</strong> Persistence rRMSE is used as a proxy for forecasting difficulty, with higher values indicating lower predictability. Results are shown for representative models (MLP, OmniVision, and ViT), with Pearson correlation coefficients reported for each lead time.</em></figcaption>
</figure>

## How cloud regime influences predictability

To explain systematic differences in predictability, we categorize cloud regimes as clear, thin, thick, or patchy based on the spatial structure and temporal evolution of cloud fields in historical sky image sequences. Regime descriptions and representative samples are shown below.

<div class="use-case-table" markdown="1">

| Cloud regime | Description |
|---|---|
| Clear | Little or no visible cloud cover |
| Thin | High-level veil clouds or smooth, diffuse cloud layers that give the sky a milky appearance |
| Thick | Dense, continuous overcast cloud cover |
| Patchy | Broken or spatially heterogeneous cloud fields, potentially involving complex cloud motion and evolution |

</div>

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_cloud_regime_examples.jpg' | relative_url }}" alt="Historical sky image sequences showing clear, thin, patchy, and thick cloud conditions at Puy de Dôme, Akwatia, Golden, and Nottingham." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Representative cloud regime examples across different sites.</strong> Sky image sequences illustrate clear, thin cloud, patchy cloud, and thick cloud conditions at Puy de Dôme, Akwatia, Golden, and Nottingham. Each example shows a 15-min historical sequence at 5-min intervals (t − 15, t − 10, t − 5, and t), highlighting cross-site differences in the visual appearance of each cloud regime.</em></figcaption>
</figure>

For each site, up to 1,000 test samples are manually labeled using historical sky image sequences. Persistence rRMSE is then calculated separately for each location, cloud regime, and forecast horizon. Our analysis highlights two main findings:

**Patchy clouds are generally the most challenging regime.** Spatially heterogeneous and rapidly evolving patchy cloud fields tend to produce the highest forecasting errors. Across locations, overall predictability also broadly follows the difficulty observed under patchy-cloud conditions.

**Patchy clouds warrant more targeted investigation.** Distinguishing errors associated with cloud motion from those caused by complex cloud evolution may help identify where improved spatial context, cloud dynamics, or physical information is needed.

These findings demonstrate how SolarBench can support a deeper understanding of solar predictability and guide the development of forecasting methods tailored to challenging atmospheric conditions.

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_cloud_regime_vs_error.jpg' | relative_url }}" alt="Persistence rRMSE across sites for clear, thin, thick, and patchy cloud regimes at 10-, 60-, and 120-minute lead times, with category medians and the overall error pattern." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Persistence error across cloud regimes and lead times.</strong> Bar plots show persistence rRMSE across sites for Clear, Thin, Thick, and Patchy cloud regimes at 10-, 60-, and 120-min lead times. Solid horizontal lines indicate category medians. Dashed lines in the Patchy panels denote the overall persistence error pattern across all cloud regimes, illustrating its close alignment with the cross-location error pattern under Patchy conditions. Representative sky image sequences for each cloud regime are shown above the first row.</em></figcaption>
</figure>
