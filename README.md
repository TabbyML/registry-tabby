# 🧑‍🔬 Tabby Registry

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**, or **Apple Silicon** like the M1.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

We have published benchmarks for these models on https://leaderboard.tabbyml.com for Tabby's users to consider when making trade-offs between quality, licensing, and model size.

| Model ID | License |
| -------- | ------- |
| [TabbyML/StarCoder-1B](https://huggingface.co/bigcode/starcoderbase-1b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/StarCoder-3B](https://huggingface.co/bigcode/starcoderbase-3b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/StarCoder-7B](https://huggingface.co/bigcode/starcoderbase-7b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/StarCoder2-3B](https://huggingface.co/bigcode/starcoder2-3b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/CodeLlama-7B](https://huggingface.co/codellama/CodeLlama-7b-hf) | [Llama 2](https://github.com/facebookresearch/llama/blob/main/LICENSE) |
| [TabbyML/CodeLlama-13B](https://huggingface.co/codellama/CodeLlama-13b-hf) | [Llama 2](https://github.com/facebookresearch/llama/blob/main/LICENSE) |
| [TabbyML/DeepseekCoder-1.3B](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [TabbyML/DeepseekCoder-6.7B](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [TabbyML/CodeGemma-2B](https://huggingface.co/google/codegemma-2b) | [Gemma License](https://ai.google.dev/gemma/terms) |
| [TabbyML/CodeGemma-7B](https://huggingface.co/google/codegemma-7b) | [Gemma License](https://ai.google.dev/gemma/terms) |
| [TabbyML/CodeQwen-7B](https://huggingface.co/Qwen/CodeQwen1.5-7B-Chat) | [Tongyi Qianwen License](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT) |


## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 3B parameters.

| Model ID | License |
| -------- | ------- |
| [TabbyML/WizardCoder-3B](https://huggingface.co/WizardLM/WizardCoder-3B-V1.0) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [TabbyML/Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |
| [TabbyML/CodeGemma-7B-Instruct](https://huggingface.co/google/codegemma-7b-it) | [Gemma License](https://ai.google.dev/gemma/terms) |
| [TabbyML/CodeQwen-7B-Chat](https://huggingface.co/Qwen/CodeQwen1.5-7B-Chat) | [Tongyi Qianwen License](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT) |
