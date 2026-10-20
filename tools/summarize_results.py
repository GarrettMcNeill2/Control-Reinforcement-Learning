#!/usr/bin/env python3
"""Summarize supplied artifacts offline. Never execute research notebooks."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def write_csv(path, rows, columns):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

def main():
    output = ROOT / 'results'
    output.mkdir(exist_ok=True)
    baseline = []
    per_task = []
    for path in sorted((ROOT / 'research/benchmark_test').glob('*.csv')):
        with path.open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        assert rows and all(row['is_correct'] in {'0', '1'} for row in rows)
        correct = sum(int(row['is_correct']) for row in rows)
        counts = Counter(row['task'] for row in rows)
        baseline.append(dict(artifact=path.name, rows=len(rows), tasks=len(counts),
                             recorded_correct=correct, recorded_accuracy=round(correct / len(rows), 6)))
        for task, count in sorted(counts.items()):
            n_correct = sum(int(row['is_correct']) for row in rows if row['task'] == task)
            per_task.append(dict(artifact=path.name, task=task, rows=count,
                                 recorded_correct=n_correct, recorded_accuracy=round(n_correct/count, 6)))
    nb = json.loads((ROOT / 'research/CRL_Demo.ipynb').read_text())
    # Concatenate text streams in cell order; ignore rich display payloads and progress bars.
    log = '\n'.join(''.join(item.get('text', [])) for cell in nb['cells']
                    for item in cell.get('outputs', []) if item.get('output_type') == 'stream')
    evaluations = []
    for match in re.finditer(r'Evaluating at step (\d+)(.*?)(?=Evaluating at step |\Z)', log, re.S):
        step, block = match.groups()
        metrics = dict(re.findall(r'\|\s*(TP|FP|FN|TN|Accuracy|Precision|Recall)\s*\|\s*([\d.]+)', block))
        if not all(key in metrics for key in ['TP', 'FP', 'FN', 'TN']):
            continue
        tp, fp, fn, tn = (int(metrics[key]) for key in ['TP', 'FP', 'FN', 'TN'])
        n = tp + fp + fn + tn
        diversity = re.search(r'Total Feature Selection Diversirty\s*:\s*(\d+)', block)
        evaluations.append(dict(step=int(step), samples=n, tp=tp, fp=fp, fn=fn, tn=tn,
                                accuracy=round((tp+tn)/n, 6),
                                positive_prediction_rate=round((tp+fp)/n, 6),
                                always_yes_accuracy=round((tp+fn)/n, 6),
                                selected_feature_count=int(diversity.group(1)) if diversity else ''))
    assert evaluations, 'No saved notebook evaluations found'
    write_csv(output/'historical-baselines.csv', baseline, list(baseline[0]))
    write_csv(output/'historical-baselines-by-task.csv', per_task, list(per_task[0]))
    write_csv(output/'notebook-evaluations.csv', evaluations, list(evaluations[0]))
    lines = ['# Results from supplied artifacts', '',
             'Generated offline with `python3 tools/summarize_results.py`. No model inference is performed.', '',
             '## Latest notebook: saved training-time evaluations', '',
             'Values below are recomputed from the confusion matrices in saved notebook output. '
             'They are historical session evidence, not a fresh execution of the current source. '
             'Each evaluation samples 100 questions with replacement; the evaluated question mix can change. '
             'The always-Yes column is computed from the labels in each confusion matrix, not a separate model run.', '',
             '| Step | Accuracy | Always Yes | Predicted Yes | Selected features |',
             '| ---: | ---: | ---: | ---: | ---: |']
    for row in evaluations:
        lines.append(f"| {row['step']} | {row['accuracy']:.0%} | {row['always_yes_accuracy']:.0%} | {row['positive_prediction_rate']:.0%} | {row['selected_feature_count']} |")
    lines += ['', 'The saved evaluations show positive-class bias and concentrated feature selection. '
              'Accuracy alone should not be interpreted as learned steering benefit. '
              'The notebook includes a later multi-checkpoint evaluation block, but it has no saved comparison output. '
              'Detailed question logs and checkpoints from these runs were not supplied.', '',
              '## Historical baseline prediction CSVs', '',
              '| File | Predictions | Observed tasks | Recorded accuracy |',
              '| --- | ---: | ---: | ---: |']
    for row in baseline:
        lines.append(f"| {row['artifact']} | {row['rows']} | {row['tasks']} | {row['recorded_accuracy']:.2%} |")
    lines += ['', 'These are sums of the existing `is_correct` flags, which use substring scoring in the historical script. '
              'They are not rescored exact-match accuracies or standardized LegalBench scores. '
              'The script lists more tasks than appear in the CSVs and catches task-load failures; '
              'only the observed rows are counted. The filenames suggest model variants but do not constitute complete run provenance.', '',
              '**Do not compare these percentages directly with the latest notebook:** the model generation, prompts, '
              'decoding, and sampled partitions differ. No improvement over baseline is claimed.', '',
              'Machine-readable details: [notebook evaluations](notebook-evaluations.csv), '
              '[baseline summary](historical-baselines.csv), '
              '[baseline task breakdown](historical-baselines-by-task.csv).', '']
    (output/'README.md').write_text('\n'.join(lines))
    print(f'Summarized {len(evaluations)} saved evaluations and {sum(row["rows"] for row in baseline)} baseline predictions.')

if __name__ == '__main__':
    main()
