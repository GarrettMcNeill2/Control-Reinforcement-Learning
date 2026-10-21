# Control Reinforcement Learning

Garrett McNeill | Summer REU

This project explores steering a language model with reinforcement learning and sparse autoencoders (SAEs). I used Gemma 2 2B for legal issue spotting: given a passage, the model answers whether it raises a particular legal issue. A separate actor-critic controller chooses an SAE feature to amplify during the model's forward pass.

The main implementation is in [CRL_Demo.ipynb](research/CRL_Demo.ipynb). It includes the steering hook, policy updates, checkpointing, and evaluation logs through training step 4,000.

## How it works

The actor reads the 2,304-dimensional residual state at layer 20 and produces scores for 16,384 SAE features. It chooses among features active on that pass, then adds the chosen feature's decoder direction to the last token's residual stream. A critic estimates the value of the state. The model's Yes/No answer supplies the reward for the controller's updates.

I used a clipped policy objective with entropy regularization and logged prediction errors, critic estimates, and feature choices to see how the controller behaved during training.

[Architecture and training settings](docs/ARCHITECTURE.md) · [Research notes](docs/RESEARCH.md)

## Results

The saved evaluations show a strong tendency to answer Yes and to choose from a small group of features. They don't establish an accuracy gain from steering. The [results page](results/README.md) includes all 17 evaluations, along with summaries of two earlier baseline runs containing 650 predictions each. Those earlier runs used different models and prompts, so their scores aren't directly comparable to the controller's results.

## Running the code

The notebook was written for Colab with a CUDA GPU. It depends on task prompts and checkpoints stored in Google Drive that aren't included here. There are also a few issues to address before running it from a fresh session, including a missing argument in an evaluation call. See the [setup and known issues](docs/REPRODUCTION.md).

To regenerate the result tables from the saved files, only Python 3 is needed:

```bash
python3 tools/summarize_results.py
```

## Files

| Folder | Contents |
| --- | --- |
| `research/` | Latest notebook, earlier prototype, and baseline predictions |
| `presentations/` | [RL and SAE talks](presentations/README.md), diagrams, and experiment notes |
| `results/` | Evaluation tables generated from the saved output |
| `learning/` | Python exercises and a C linked-list exercise from the start of the summer |
| `tools/` | Scripts for summarizing results and checking file hashes |
| `docs/` | Implementation details, setup notes, and sources |

The research files are unchanged from the originals. `python3 tools/verify_sources.py` checks them against the recorded hashes.

The presentations cite earlier research, and the Python exercises retain Google's license and reference solutions. See [sources and attribution](docs/PROVENANCE.md) for details.
