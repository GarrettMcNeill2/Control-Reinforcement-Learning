# Research notes

I wanted to test whether a small controller could improve legal issue spotting by choosing which SAE features to amplify. Keeping track of those choices also gave me a way to inspect what the controller was doing.

My initial plan was to compare base and instruction-tuned models, then see whether CRL could close the gap. I also wanted to test how a controller trained on one task would perform on others.

## Implementation

[CRL_Demo.ipynb](../research/CRL_Demo.ipynb) loads `google/gemma-2-2b` in 4-bit precision and uses the Gemma Scope residual SAE for layer 20, with 16,384 features. The actor reads the residual state and selects an active feature. A forward hook adds that feature's decoder direction to the final token's residual stream.

The model can generate only Yes or No. A correct answer earns a reward of 1, and an incorrect answer earns 0. The controller uses these rewards to update the actor and critic. The notebook also saves checkpoints and records predictions, feature choices, and critic estimates during evaluation.

## What I observed

The saved evaluations show that the model answered Yes much more often than No. The controller also tended to select the same few features. The confusion matrices and feature counts made both patterns visible, even when the overall accuracy changed between evaluations.

There is more work to do before attributing any improvement to steering. The earlier baseline runs use different models and prompts. A useful comparison would run the same model on the same questions with steering turned on and off, keeping the prompt and decoding settings fixed.

The final 20% of the notebook's split is sampled repeatedly during training. A separate test set would be needed for a final evaluation. Feature IDs also need further investigation before drawing conclusions about what the selected directions represent.

[Saved results](../results/README.md) · [Setup and known issues](REPRODUCTION.md)
