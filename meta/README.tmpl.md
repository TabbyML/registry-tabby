# 🧑‍🔬 Tabby Registry

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**, or **Apple Silicon** like the M1.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

We have published benchmarks for these models on https://leaderboard.tabbyml.com for Tabby's users to consider when making trade-offs between quality, licensing, and model size.

| Model ID | License |
| -------- | ------- |
{% for item in completion_models %}| [{{ item.name }}]({{ item.provider_url }}) | [{{ item.license_name }}]({{ item.license_url }}) |
{% endfor %}

## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 1B parameters.

| Model ID | License |
| -------- | ------- |
{% for item in chat_models %}| [{{ item.name }}]({{ item.provider_url }}) | [{{ item.license_name }}]({{ item.license_url }}) |
{% endfor %}

## Embedding models

| Model ID | License |
| -------- | ------- |
{% for item in embedding_models %}| [{{ item.name }}]({{ item.provider_url }}) | [{{ item.license_name }}]({{ item.license_url }}) |
{% endfor %}
