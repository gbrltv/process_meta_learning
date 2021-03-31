# Meta-Learning applied to Process Mining

> Application of Meta-learning to recommend a suitable process discovery method that maximizes model quality in four complementary dimensions: fitness, precision, generalization and simplicity. According to our Meta-learning pipeline, it is possible to recommend a discovery method with 92% of accuracy using light-weight meta-features from the Process Mining domain.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/gbrltv/process_meta_learning/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/gbrltv/process_meta_learning)](https://img.shields.io/github/issues/gbrltv/process_meta_learning)
[![GitHub forks](https://img.shields.io/github/forks/gbrltv/process_meta_learning)](https://github.com/forks/gbrltv/process_meta_learning)
[![GitHub stars](https://img.shields.io/github/stars/gbrltv/process_meta_learning)](https://img.shields.io/github/stars/gbrltv/process_meta_learning)
[![GitHub license](https://img.shields.io/github/license/gbrltv/process_meta_learning)](https://img.shields.io/github/license/gbrltv/process_meta_learning)

## Table of Contents

- [Installation](#installation)
- [Experimental Setup](#experimental-setup)
  - [Data preparation](#data-preparation)
  - [Extracting Meta-features](#extracting-meta-features)
  - [Model Quality Metrics](#model-quality-metrics)
  - [Evaluating Results](https://github.com/gbrltv/process_meta_learning/blob/main/evaluation.ipynb)
- [References](#references)
- [Contributors](#contributors)

## Installation

### Clone

Clone this repo to your local machine using

```shell
git clone https://github.com/gbrltv/process_meta_learning.git
```

## Experimental Setup

### Data preparation


Before running the experiments, it is necessary to convert the original logs (`xes.gz`) to the `xes` format (entropy extraction does not accept `xes.gz` files). For that, run:

```shell
python3 convert_log_files.py
```

This code converts files under the `event_logs` folder and removes the original files.


### Extracting Meta-features

To extract the meta-features from event logs, simply run the following line of code:

```shell
python3 extract_features.py
```

The meta-features are saved under the `results` folder with the name `log_features.csv`.


### Model Quality Metrics

To compute model quality metrics (fitness, precision, generalization, simplicity), run the following code:


```shell
python3 model_metrics.py
```

The quality metrics (along with their computation time) are saved under the `results` folder with the name `model_metrics.csv`.

### Evaluating Results

For an in-depth analysis of results, classification performance, model relevance, and quality metrics, please take a look [here](https://github.com/gbrltv/process_meta_learning/blob/main/evaluation.ipynb).

## References

[Barbon Jr., S., Ceravolo, P., Damiani, E., Tavares, G.M.: Using Meta-learning to Recommend Process Discovery Methods, 2021](https://arxiv.org/abs/2103.12874)

## Contributors

- [Gabriel Marques Tavares](https://www.researchgate.net/profile/Gabriel_Tavares6), PhD candidate at Università degli Studi di Milano
- [Paolo Ceravolo](https://www.unimi.it/en/ugov/person/paolo-ceravolo), Associate Professor at Università degli Studi di Milano
- [Sylvio Barbon Junior](http://www.barbon.com.br/), Associate Professor at State University of Londrina
