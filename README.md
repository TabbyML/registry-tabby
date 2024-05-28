# 🧑‍🔬 Tabby Registry

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

| Model ID | License |
| -------- | ------- |
| [colefuerth/StarCoder-3B](https://huggingface.co/bigcode/starcoderbase-3b) | [BigCode-OpenRAIL-M](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement) |
| [colefuerth/DeepseekCoder-1.3B](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [colefuerth/DeepseekCoder-5.7bmqa-base-Q8_0](https://huggingface.co/deepseek-ai/deepseek-coder-5.7bmqa-base) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [colefuerth/DeepseekCoder-6.7B-instruct-Q5_K_S](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [colefuerth/DeepseekCoder-6.7B-instruct-Q6_K](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | [Deepseek License](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) |
| [colefuerth/OpenLlama-3B-instruct-V2-Q6_K](https://huggingface.co/codellama/CodeLlama-7b-hf) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |
| [colefuerth/OpenLlama-3B-instruct-V2-Q8_0](https://huggingface.co/codellama/CodeLlama-7b-hf) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |


## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 3B parameters.

| Model ID | License |
| -------- | ------- |
| [colefuerth/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |
| [colefuerth/Open_Gpt4_8x7B_v0.2-Q6_K](https://huggingface.co/rombodawg/Open_Gpt4_8x7B_v0.2) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) |
