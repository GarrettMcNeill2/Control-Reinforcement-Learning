# Research questions

This project explores CRL on LegalBench, outside the task set evaluated in the original paper.

- Can the method be reproduced on legal issue spotting?
- Does the controller select features with meanings related to the task?
- How do rewards, learning rates, and entropy regularization affect feature selection?
- How does steering affect task performance?

The experiments use Gemma 2 2B, a layer-20 Gemma Scope SAE, and actor–critic networks trained with PPO. The notebook records feature selections alongside answers and critic estimates.

The poster reports changes in feature diversity across implementation variants, with smaller changes in model scores. It identifies other layers, cross-task performance, and controllers at multiple layers as directions for further work.

[Results](../results/README.md) · [Poster](../demo/poster.pdf)
