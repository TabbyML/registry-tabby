# 🧑‍🔬 Tabby Registry

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

| Model ID | License |
| -------- | ------- |
| [TabbyML/StarCoder-3B](https://huggingface.co/bigcode/starcoderbase-3b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/DeepseekCoder-5.7bmqa-base-Q8_K](https://huggingface.co/deepseek-ai/deepseek-coder-5.7bmqa-base) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [TabbyML/DeepseekCoder-6.7B-instruct-Q6_K](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |


## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 3B parameters.

| Model ID | License |
| -------- | ------- |
