# Results from supplied artifacts

Generated offline with `python3 tools/summarize_results.py`. No model inference is performed.

## Latest notebook: saved training-time evaluations

Values below are recomputed from the confusion matrices in saved notebook output. They are historical session evidence, not a fresh execution of the current source. Each evaluation samples 100 questions with replacement; the evaluated question mix can change. The always-Yes column is computed from the labels in each confusion matrix, not a separate model run.

| Step | Accuracy | Always Yes | Predicted Yes | Selected features |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 50% | 55% | 95% | 5 |
| 250 | 48% | 53% | 91% | 5 |
| 500 | 34% | 40% | 94% | 8 |
| 750 | 47% | 49% | 94% | 5 |
| 1000 | 46% | 47% | 93% | 7 |
| 1250 | 52% | 54% | 96% | 6 |
| 1500 | 54% | 52% | 94% | 6 |
| 1750 | 44% | 44% | 94% | 6 |
| 2000 | 49% | 51% | 96% | 7 |
| 2250 | 54% | 57% | 97% | 5 |
| 2500 | 53% | 53% | 98% | 8 |
| 2750 | 47% | 45% | 98% | 7 |
| 3000 | 57% | 58% | 97% | 5 |
| 3250 | 44% | 49% | 95% | 7 |
| 3500 | 52% | 57% | 91% | 10 |
| 3750 | 42% | 44% | 96% | 5 |
| 4000 | 52% | 53% | 93% | 6 |

The saved evaluations show positive-class bias and concentrated feature selection. Accuracy alone should not be interpreted as learned steering benefit. The notebook includes a later multi-checkpoint evaluation block, but it has no saved comparison output. Detailed question logs and checkpoints from these runs were not supplied.

## Historical baseline prediction CSVs

| File | Predictions | Observed tasks | Recorded accuracy |
| --- | ---: | ---: | ---: |
| gemma2b_it_lb_issue_spotting_results.csv | 650 | 13 | 90.15% |
| gemma2b_lb_issue_spotting_results.csv | 650 | 13 | 70.31% |

These are sums of the existing `is_correct` flags, which use substring scoring in the historical script. They are not rescored exact-match accuracies or standardized LegalBench scores. The script lists more tasks than appear in the CSVs and catches task-load failures; only the observed rows are counted. The filenames suggest model variants but do not constitute complete run provenance.

**Do not compare these percentages directly with the latest notebook:** the model generation, prompts, decoding, and sampled partitions differ. No improvement over baseline is claimed.

Machine-readable details: [notebook evaluations](notebook-evaluations.csv), [baseline summary](historical-baselines.csv), [baseline task breakdown](historical-baselines-by-task.csv).
