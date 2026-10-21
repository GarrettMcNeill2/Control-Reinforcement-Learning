# Project discussion notes

I used a sparse autoencoder to give a reinforcement learning controller a set of features it could choose to amplify. The controller reads Gemma's residual state, chooses a feature, and adds its decoder direction back into the residual stream. Legal issue spotting gave me a binary answer to use as a reward.

Most of the implementation is in the Colab notebook: the actor and critic, the hook into the model, policy updates, checkpoints, and evaluation functions. I also prepared talks on RL fundamentals and the SAE steering method.

The evaluation logs raised two questions: why the model was answering Yes so often, and why the controller kept choosing the same few features. A next experiment would compare steering on and off with fixed prompts and an untouched test set.

## Questions to investigate

- How sensitive is steering to the layer and coefficient?
- How does resetting the feature mask on each pass affect exploration?
- What do the frequently selected features represent?
- How much of the positive-class bias comes from the prompt or base model?
- Would a controller trained on one legal task transfer to another?
