# Results

These tables come from the saved notebook output and baseline CSVs. Rebuild them with `python3 tools/summarize_results.py`.

## Latest notebook: saved training-time evaluations

The values below come from the confusion matrices saved in the notebook. The notebook has not been rerun to produce this table. Each evaluation samples 100 questions with replacement; the evaluated question mix can change. The always-Yes column is computed from the labels in each confusion matrix, not a separate model run.

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

The model usually answered Yes, and the controller selected from a small group of features. These results do not establish an accuracy gain from steering. The notebook includes a later multi-checkpoint evaluation block, but it has no saved comparison output. The question logs and checkpoints from these runs are missing.

## Historical baseline prediction CSVs

| File | Predictions | Observed tasks | Recorded accuracy |
| --- | ---: | ---: | ---: |
| gemma2b_it_lb_issue_spotting_results.csv | 650 | 13 | 90.15% |
| gemma2b_lb_issue_spotting_results.csv | 650 | 13 | 70.31% |

Accuracy is the fraction of rows marked `is_correct` in each CSV. The script uses substring matching rather than exact-match scoring. The script lists more tasks than appear in the CSVs and catches task-load failures; only the observed rows are counted. The filenames identify the model variants, but the full run settings were not saved.

The baseline runs and the latest notebook use different models, prompts, decoding settings, and samples, so their scores cannot be compared directly.

CSV files: [notebook evaluations](notebook-evaluations.csv), [baseline summary](historical-baselines.csv), [baseline task breakdown](historical-baselines-by-task.csv).
