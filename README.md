# Interpretable LLM Steering with Reinforcement Learning

**Garrett McNeill · Summer REU research portfolio**

I explored whether a reinforcement learning controller could steer a language model by selecting interpretable sparse autoencoder (SAE) features. The main experiment targets binary legal issue spotting with Gemma 2 2B and LegalBench.

The work combines a PyTorch actor–critic controller, transformer activation hooks, constrained decoding, checkpointing, and diagnostics for feature selection and model predictions.

## Start here

| If you have… | Open | What you will see |
| --- | --- | --- |
| 2 minutes | [Research overview](docs/RESEARCH.md) | Question, implementation, and what the evidence supports |
| 5 minutes | [Latest notebook](research/CRL_Demo.ipynb) | Controller implementation and saved training diagnostics |
| 10 minutes | [Results](results/README.md) | Extracted notebook evaluations and historical baseline summaries |
| A technical interview | [Architecture](docs/ARCHITECTURE.md) | How the intervention and policy update fit together |
| Interest in the presentations | [Presentation guide](presentations/README.md) | RL foundations, CRL literature, and experiment planning |

## What I built

- An actor that maps the 2,304-dimensional residual state to logits over 16,384 SAE features, with a separate value critic.
- A controller that masks feature choices to currently active SAE features and adds a selected decoder direction to the last token's residual stream at layer 20.
- A clipped policy objective with entropy regularization, critic regression, buffered updates, and gradient clipping.
- Evaluation and logging for binary predictions, confusion matrices, selected features, and critic values, plus Google Drive checkpoint save/load support.

## Evidence and current status

The latest notebook contains saved evaluation logs through training step 4,000. These show a functioning experimental workflow in the saved session, but do not establish an improvement over an unsteered model. The historical baseline CSVs contain **650 predictions each**, under a different model/prompt setup.

The supplied notebook depends on external task prompt files and Drive checkpoints. Its current source also contains an evaluation-call mismatch. Read [reproduction notes](docs/REPRODUCTION.md) before running it. No GPU training was rerun during repository preparation.

## Repository map

```text
research/          Latest notebook, historical prototype, and baseline artifacts
presentations/     Original talks, experiment notes, and architecture PDFs
results/           Reproducible summaries of supplied artifacts
learning/          Python course exercises and C linked-list material
tools/            Offline analysis and source-integrity verification
docs/             Research narrative, architecture, provenance, and interview notes
```

## Inspect the results locally

Python 3 is enough to regenerate the summaries; no model downloads or GPU are required:

```bash
python3 tools/summarize_results.py
python3 tools/verify_sources.py
```

The original notebooks, presentations, code, and CSVs are copied byte for byte. New documentation and analysis utilities were added for presentation. The earlier notebook remains in `research/archive/`.

## Attribution

The CRL presentations discuss prior research; numerical results quoted from that literature are not results from this project. The historical benchmark script explicitly records AI assistance in its header. Google's Python exercise scaffolding and supplied solutions retain their Apache 2.0 license and notice. Learning materials are included as context, with no claim that third-party scaffolding or reference solutions are original research.

See [provenance and rights](docs/PROVENANCE.md). No repository-wide license has been applied.
