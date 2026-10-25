# Control Reinforcement Learning

Garrett McNeill · REU 2026

An exploration of Control Reinforcement Learning (CRL) on LegalBench. This work investigates whether the method can be reproduced on tasks outside the original paper’s evaluation and how reward functions, learning rates, and entropy regularization affect feature selection.

[Interactive demonstration](https://garrettmcneill2.github.io/Control-Reinforcement-Learning/) · [Research poster](demo/poster.pdf) · [Experiment notebook](research/CRL_Demo.ipynb)

## Method

CRL intervenes in a language model’s forward pass at a selected layer. A sparse autoencoder (SAE) exposes features in the residual stream. An actor selects a feature direction to amplify, and the modified residual returns to the remaining transformer layers. Task rewards train the actor and critic with PPO while the language-model weights remain fixed.

## Experiment

I applied CRL to Learned Hands issue-spotting tasks from LegalBench using Gemma 2 2B and a layer-20 Gemma Scope SAE with 16,384 features. The controller uses top-1 selection and trains for 4,000 steps. Experiments compare learning rates, incorrect-answer penalties, and entropy regularization.

The main questions were whether the controller would learn feature-selection behavior on this task and whether training choices would change its diversity and selected features.

## Findings

The experiments reproduced feature-selection behavior on a task outside the original paper’s evaluation. Changing the reward, learning rate, and entropy term affected feature diversity and sometimes the learned selection policy. Model scores varied less than feature diversity across these runs.

[Poster results](results/README.md) · [Method details](docs/ARCHITECTURE.md) · [Research discussion](docs/RESEARCH.md)

## Materials

- `demo/`: interactive method explanation and final poster.
- `research/CRL_Demo.ipynb`: controller, intervention hook, training, and evaluation.
- `research/archive/`: earlier experiment notebook.
- `research/benchmark_test/`: initial benchmark code and recorded predictions.
- `presentations/`: RL background, CRL literature, and experiment planning.

[Sources and attribution](docs/PROVENANCE.md)
