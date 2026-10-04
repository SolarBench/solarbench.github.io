---
title: Get Started
layout: home
nav_order: 6
---

<link rel="stylesheet" href="{{ '/assets/css/get-started.css' | relative_url }}?v={{ site.time | date: '%s' }}">

<div class="datasets-heading">
  <h1>Get Started</h1>
  <div class="datasets-actions">
    <a href="https://solarbench.readthedocs.io/" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Toolbox documentation</a>
    <a href="https://github.com/Solar4cast/solarbench" class="btn" target="_blank" rel="noopener noreferrer">GitHub repository</a>
  </div>
</div>

Get started by installing the `solarbench` Python package and exploring basic functions for accessing datasets, preparing forecasting samples, and evaluating predictions.

## Installation

From PyPI (available soon):

```bash
pip install solarbench
```

## Demo

The notebook below demonstrates basic functions of the `solarbench` toolbox.


<iframe class="notebook-embed" src="{{ '/assets/notebooks/solarbench_demo.html' | relative_url }}" title="SolarBench demo notebook with saved outputs" loading="lazy"></iframe>
