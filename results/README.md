# CRL experiment results

The experiment evaluates CRL on Learned Hands issue spotting from LegalBench. The comparison tests whether different training choices change feature-selection diversity and the learned policy.

## Implementation variants

| Test run | Mean score (%) | Feature diversity |
| --- | ---: | ---: |
| Baseline | 48.33 ± 1.77 | — |
| Initial | 51.67 ± 0.72 | 3.66 ± 0.94 |
| Incorrect reward −10 | 51.45 ± 1.49 | 7.00 ± 0.82 |
| Learning rate 5 × 10⁻⁶ | 51.78 ± 0.63 | 16.33 ± 1.70 |
| Lower rate + incorrect reward −10 | 50.33 ± 1.51 | 26.67 ± 0.94 |
| Lower rate + entropy | 50.89 ± 1.64 | 12.66 ± 0.94 |

Values and ± notation follow the [final research poster](../demo/poster.pdf).

## Feature selection

The controller learned feature-selection behavior on tasks outside the original CRL evaluation. Reward penalties, learning rates, and entropy regularization changed selection diversity and sometimes the features selected. The lower-rate penalty run produced the highest diversity in this comparison.

The poster includes the following selected-feature descriptions:

| Feature | Description |
| --- | --- |
| 1891 | “first” and related phrases describing initial achievements or events |
| 6627 | Prominent names and references related to social issues or health crises |
| 8170 | Security and privacy in data handling |
| 14774 | Technical terms and structured data formats |

## Further experiments

The poster proposes testing other SAE layers, models, tasks, and hyperparameters; cross-task evaluation; controllers at multiple layers; and multiple task objectives.
