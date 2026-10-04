---
title: About
layout: home
nav_order: 3
---

# About the initiative

## Why solar nowcasting matters

Solar PV is playing an increasingly important role in the energy transition. However, solar power generation can fluctuate sharply due to rapidly changing local weather conditions, particularly cloud cover, creating operational challenges as solar deployment increases.

<figure style="max-width: 800px; margin: 24px auto;">
<video autoplay muted loop controls playsinline preload="metadata" poster="{{ '/assets/imgs/intermittency_eg_poster.png' | relative_url }}" width="1200" height="300" aria-describedby="intermittency-caption" style="display: block; width: 100%; height: auto;">
  <source src="{{ '/assets/imgs/intermittency_eg.mp4' | relative_url }}?v=faststart-1" type="video/mp4">
  Your browser does not support embedded video. <a href="{{ '/assets/imgs/intermittency_eg.mp4' | relative_url }}?v=faststart-1">Download the video</a>.
</video>
<figcaption id="intermittency-caption" style="margin-top: 8px; font-size: 0.875rem; font-style: italic;">Power output from a 30-kW rooftop PV system on a partly cloudy day, illustrating rapid fluctuations as clouds pass overhead. Imagine the impact of similar fluctuations at a gigawatt-scale solar farm. </figcaption>
</figure>

Solar nowcasting aims to predict solar irradiance or PV output **over horizons ranging from minutes to a few hours**. Reliable nowcasts reduce uncertainty in solar generation, supporting more informed operational and economic decisions in applications such as real-time grid balancing, energy trading, and flexible demand coordination. It serves as an essential tool for enabling large-scale solar integration.

## Do reported advances generalize

State-of-the-art approaches increasingly apply deep learning to sky camera and geostationary satellite observations. But do improvements demonstrated at one site hold across other climates, cloud regimes, and PV systems?

Answering this question is difficult because existing datasets often cover only one or a few sites and differ in sampling frequency, record length, and available measurements. Studies also use different processing workflows, forecasting tasks, data splits, baselines, and metrics. **These differences make it difficult to separate improvements in model capability from differences in forecasting difficulty and experimental setup.**

We built SolarBench to address this gap by bringing together harmonized multimodal data, standardized forecasting tasks, and reproducible workflows for model development and evaluation. This shared framework enables consistent comparisons across locations, atmospheric conditions, and PV systems, helping researchers understand where methods work well and where further progress is needed.

## Who SolarBench is for

- **Forecasting researchers** developing and comparing methods for solar irradiance and PV power nowcasting.
- **Machine learning researchers** studying multimodal learning, generalization across locations, and adaptation with limited training data.
- **Industry users** investigating forecasting performance under variable conditions and data requirements for adapting models to new PV systems.

## Our vision

We envision SolarBench as a shared, extensible foundation for advancing solar nowcasting research and applications. Through community contributions, we aim to expand its geographic coverage and continually incorporate new datasets, models, evaluation metrics, and forecasting tasks. Beyond accuracy metrics, an important future direction is to connect model evaluation with real-world operational and economic outcomes, such as energy storage dispatch and grid management. Ultimately, we hope to foster a collaborative research ecosystem that accelerates methodological innovation, improves model generalizability, and bridges the gap between forecasting research and practical deployment to support reliable, large-scale solar integration.

## The team

**Massachusetts Institute of Technology**: Yuhao Nie (Project Lead), Stephen Campbell, Jonathan Giezendanner, and Sherrie Wang.<br>
**European Space Agency**: Quentin Paletta.<br>
**Stanford University**: Andea Scott, Tao Sun, and Adam Brandt.<br>
**University of Nottingham**: Liwenbo Zhang, Yuexing Yang, Yang Ming, and Yupeng Wu.<br>
**Hochschule Bonn-Rhein-Sieg University of Applied Sciences**: Samer Chaaraoui, and Stefanie Meilinger.<br>
**Hong Kong Polytechnic University**: Tao Jing, and Mengying Li.<br>
**University of Texas at Dallas**: Cong Feng.<br>
**Mines Paris — PSL**: Max Aragon.<br>
**Technical University of Denmark**: Adam Jensen.<br>
**OFFIS - Institute for Information Technology**: Florian Kotthoff.<br>
**Independent researcher**: Jacques Camier.

## Acknowledgements
We gratefully acknowledge funding from Eni through its membership in the MIT Energy Initiative, as well as support from the ESA Φ-lab and Climate Office. We also acknowledge the UK Engineering and Physical Sciences Research Council, the UK Department for Energy Security and Net Zero, The Hong Kong Polytechnic University, and the German Federal Ministry of Education and Research for supporting the collection and preparation of newly contributed observations incorporated into SolarBench. We also thank those who supported data collection for the EnerSHelF datasets in Akwatia and Kologo, Ghana, including the project partners of the Father Franz Kruse Solar Energy Project; the management and staff of St. Dominic’s Hospital in Akwatia and the Kologo Health Clinic; and the citizens of Kologo.

SolarBench also builds on existing open datasets. We are grateful to the researchers, institutions, and data providers who have dedicated substantial efforts to collecting, maintaining, processing, and openly sharing environmental and solar energy data. Their contributions form an essential part of SolarBench and help make solar nowcasting research more accessible to the broader community.

We look forward to continued collaboration with the community.
