# 🧑‍🔬 Tabby Registry

## Completion models (`--model`)

We recommend using

* For **1B to 3B models**, it's advisable to have at least **NVIDIA T4, 10 Series, or 20 Series GPUs**, or **Apple Silicon** like the M1.
* For **7B to 13B models**, we recommend using **NVIDIA V100, A100, 30 Series, or 40 Series GPUs**.

| Model ID | License |
| -------- | ------- |
{% for item in completion_models %}| [TabbyML/{{ item.name }}]({{ item.provider_url }}) | [{{ item.license_name }}]({{ item.license_url }}) |
{% endfor %}

## Chat models (`--chat-model`)

To ensure optimal response quality, and given that latency requirements are not stringent in this scenario, we recommend using a model with at least 3B parameters.

| Model ID | License |
| -------- | ------- |
{% for item in chat_models %}| [TabbyML/{{ item.name }}]({{ item.provider_url }}) | [{{ item.license_name }}]({{ item.license_url }}) |
{% endfor %}
