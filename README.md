# 🧑‍🔬 Tabby Registry for `TabbyML` org.

---

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

| Model ID | License |
| -------- | ------- |
| TabbyML/StarCoder-1B | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| TabbyML/StarCoder-3B | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| TabbyML/StarCoder-7B | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| TabbyML/CodeLlama-7B | [Llama 2](https://github.com/facebookresearch/llama/blob/main/LICENSE) |
| TabbyML/CodeLlama-13B | [Llama 2](https://github.com/facebookresearch/llama/blob/main/LICENSE) |


## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 3B parameters.

| Model ID | License |
| -------- | ------- |
| TabbyML/Mistral-7B | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |
| TabbyML/WizardCoder-3B | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| TabbyML/WizardCoder-34B | [Llama 2](https://github.com/facebookresearch/llama/blob/main/LICENSE) |
