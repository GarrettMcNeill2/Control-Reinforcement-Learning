# Reproduction and validation

## Offline review

From the repository root, run:

```bash
python3 tools/summarize_results.py
python3 tools/verify_sources.py
```

These commands read local artifacts only. The verifier compares every copied artifact with its recorded SHA-256. It does not require access to the original folders.

## Main notebook environment

The notebook targets Google Colab, a CUDA GPU, Google Drive, and authenticated Hugging Face model access. It imports PyTorch, Transformers, Accelerate, bitsandbytes, datasets, pandas, tqdm, SAE Lens, huggingface_hub, NumPy, and matplotlib. Its install cell omits explicit installation of PyTorch and matplotlib, relying on the Colab environment. Package versions were not pinned in the supplied material, so this repo does not invent a tested lockfile.

To prepare a future run, make a working copy of `research/CRL_Demo.ipynb`, select a GPU runtime, configure the Colab secret `HF_TOKEN`, obtain model access, and use a new Drive output directory. The notebook writes logs and checkpoints to the configured Drive paths.

### Inputs that were not supplied

- One task prompt `.txt` per task under the notebook's `PROMPT_DIR`.
- Drive model checkpoints referenced by the optional comparison block.
- The original package/environment snapshot and row-level evaluation exports from the latest notebook run.

Do not substitute newly written prompts and call the result an exact reproduction of the saved experiment.

### Source issues to resolve in a working copy

- `training_eval(samples, model, CRLAgent, seed)` requires four arguments; the training loop passes three. The saved output therefore reflects an earlier in-memory definition or source state.
- SAE loading uses a tuple-return API that emits a deprecation warning in the saved output. Confirm the installed SAE Lens API before running.
- Only Python's RNG is seeded; PyTorch/NumPy randomness and GPU nondeterminism are not fully controlled. Evaluation reseeds Python's global RNG, which also affects later training sampling.
- Evaluation calls `.lower()` without assigning its result. Correctness uses substring matching, while confusion-matrix logic expects exact capitalized labels.
- The last 20% partition is repeatedly sampled with replacement during training evaluation. Reserve an untouched test set before reporting final generalization.
- Re-running hook registration cells can accumulate hooks. The optional checkpoint comparison block also attaches another hook without removing the original.
- `load_checkpoint` prints a warning and returns `None` when a checkpoint is absent. The optional comparison block cannot run with missing checkpoints.
- The mask is created on CPU while actor logits may be on GPU. Verify device placement and residual tensor shapes on the actual runtime.

Original artifacts remain unchanged. These are observations for future work, not patches applied to the research.

## Historical baselines

`research/benchmark_test/issue_spotting_gem1.py` names `google/gemma-2b-it` and suggests switching to `google/gemma-2b`. These differ from the latest notebook's Gemma 2 model. The supplied CSV filenames identify base versus instruction-tuned runs but provide no full run configuration.

The historical script takes the first 50 examples per successful task, catches task errors, uses a generic prompt without naming the legal issue, and scores `ground_truth in generated_text`. The output CSV filenames differ from the script's default output name. Treat the CSVs as historical artifacts, not fully reproduced benchmark runs.

## Checks during packaging

Source-integrity verification and local summary generation are the core packaging checks. No model inference, remote downloads, or GPU training is required for them. See `VALIDATION.md` for the checks actually completed.
