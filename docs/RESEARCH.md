# Research overview

## Question

Can a learned controller improve legal issue spotting by selecting SAE features to amplify during inference, while exposing which features it chose?

The experiment notes propose comparing base and instruction-tuned models, then testing whether CRL can narrow the gap. They also propose cross-task evaluation. These are research goals, rather than demonstrated outcomes.

## Implementation

The main artifact is [CRL_Demo.ipynb](../research/CRL_Demo.ipynb). It loads `google/gemma-2-2b` with 4-bit quantization and a Gemma Scope residual SAE at layer 20 with a 16k feature dictionary. An actor and critic operate on the residual state. The actor selects a feature from those active on the current pass, and a forward hook injects its decoder direction into the final token's residual stream.

The controller uses reward from a constrained Yes/No prediction to update the policy and value function. It records feature choices and critic estimates, saves checkpoints, and evaluates periodically during training.

## What the supplied artifacts demonstrate

- A substantially developed notebook with steering, policy updates, diagnostics, and saved training output.
- A research progression from RL fundamentals to SAE steering and an applied evaluation design.
- Two historical LegalBench prediction files with row-level model outputs, labels, and correctness flags.

## Interpretation

Saved notebook evaluations show frequent positive predictions and concentrated selection of a small set of features. These diagnostics are useful for investigating class bias and policy concentration. They do not, by themselves, show that the selected features have the semantic meanings intended or that steering improves performance.

The notebook and baseline runs use different model identifiers and prompting. A credible improvement claim requires matched prompts, decoding, held-out examples, and a steering-off control. The notebook's final 20% partition is consulted repeatedly during training, so it functions as a development evaluation set rather than a pristine final test set.

See [results](../results/README.md) for exact extracted values and [reproduction notes](REPRODUCTION.md) for limitations.
