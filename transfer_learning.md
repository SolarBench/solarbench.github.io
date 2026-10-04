---
title: Transfer Learning
layout: home
nav_order: 1
parent: Use Cases
---

<link rel="stylesheet" href="{{ '/assets/css/use-case-tables.css' | relative_url }}?v={{ site.time | date: '%s' }}">

# Transfer Learning to New PV Systems

Irradiance observations are more widely available than PV generation data, which are often limited by ownership, privacy, and security constraints. This creates a practical deployment challenge: a model can learn to predict irradiance from multiple sites, but a new PV system may have little local generation data for training. It remains uncertain how readily an irradiance nowcasting model can adapt to predicting power output at such a system.

SolarBench uses its geographically distributed irradiance datasets to examine whether pre-training can reduce the amount of local PV data needed for this adaptation.

## Transfer learning setup

We evaluate a two-stage approach using a Vision Transformer (ViT):

1. **Multi-site pre-training:** Train the model to nowcast GHI using observations from SolarBench sites.
2. **Local fine-tuning:** Adapt the pre-trained model to nowcast PV power using a limited amount of data from the target system.

We compare pre-training on **1, 3, or 6 source sites** drawn from Golden, Folsom, Hong Kong, Sankt Augustin, Paris, and Nottingham. The model is then fine-tuned on two PV systems that differ substantially in capacity and design: a 30 kW rooftop solar PV system at Stanford University in the US, and the 3.275 MW Gatton Solar Research Facility in Australia, which includes multiple PV arrays with different mounting and tracking configurations.

For each target system, we compare the fine-tuned model with a model trained from scratch using the same amount of local PV data. A model trained from scratch on the full local dataset provides an additional reference.

## Key findings

Pre-training on geographically diverse irradiance data improves adaptation to both PV systems. As the number of source sites increases, the fine-tuned models generally achieve better forecast skill with less local PV data. In these experiments, multi-site pre-training and local fine-tuning **reduce the local data requirement by over 50%**.

Importantly, this benefit holds across two markedly different PV systems in scale and design, demonstrating that knowledge learned from irradiance nowcasting can support site-specific PV nowcasting when local data are limited.

<figure style="max-width: 1000px; margin: 24px auto;">
  <img src="{{ '/assets/imgs/Fig_transfer_learning.jpg' | relative_url }}" alt="Stanford and Gatton PV systems and forecast skill as a function of local fine-tuning data for models pre-trained on one, three, or six irradiance sites and a local baseline." loading="lazy" decoding="async" style="display: block; width: 100%; height: auto;">
  <figcaption style="margin-top: 8px; color: #586573; font-size: 0.875rem;"><em><strong>Transfer learning from geographically distributed irradiance forecasting datasets to two real-world PV systems:</strong> a 30 kW rooftop PV installation at Stanford University, USA, and a 3.275 MW hybrid PV system at the Gatton Solar Research Facility at the University of Queensland, Australia. Pre-training on geographically distributed irradiance data followed by local fine-tuning substantially reduces local PV data requirements while maintaining competitive forecasting performance.</em></figcaption>
</figure>
