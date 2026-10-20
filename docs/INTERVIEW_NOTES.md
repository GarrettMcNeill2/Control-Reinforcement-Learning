# Interview and resume notes

## Project description

Explored interpretable LLM steering during a summer REU by implementing a PyTorch actor–critic controller over sparse autoencoder features in Gemma 2 2B, with LegalBench issue spotting as the experimental task.

## Resume bullet options

- Implemented a PyTorch controller that selects among 16,384 SAE features and steers layer-20 Gemma 2 2B residual activations using a clipped policy objective and a value critic.
- Built an experimental workflow with quantized model loading, constrained Yes/No decoding, checkpoint save/load, and diagnostics for prediction errors, critic estimates, and feature-selection concentration.
- Presented reinforcement learning foundations and SAE steering research, and investigated legal issue spotting with saved baseline predictions and training-time evaluation logs.

These bullets describe visible implementation work. Avoid adding performance improvements, production deployment, publication, or energy savings unless separately supported.

## A short walkthrough

“I wanted to understand whether a small learned controller could steer a language model through interpretable features. I used a sparse autoencoder at a transformer layer to identify available features, then trained an actor–critic controller to choose a decoder direction to amplify. I built the hook, training updates, checkpoints, and logging in a Colab notebook. The saved diagnostics show strong positive-class bias and concentrated feature selection, so the result is an experimental investigation rather than a demonstrated accuracy gain. My next step would be a matched steering-off control with fixed prompts and an untouched test set.”

## Questions worth preparing for

- Why steer activations rather than update the language model's weights?
- Why choose the last token, layer 20, and a fixed coefficient of 50?
- How does resetting the feature mask each pass change exploration?
- What can feature IDs tell you, and what additional evidence is needed for semantic interpretation?
- How would you separate class bias, prompt effects, and steering effects?
- Why are the historical baseline CSVs not a fair direct comparison to the latest notebook?
