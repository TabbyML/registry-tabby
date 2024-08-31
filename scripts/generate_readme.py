#!/usr/bin/env python3

import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("meta/README.tmpl.md")

with open("models.json", "r") as f:
    models = json.load(f)

completion_models = [x for x in models if 'prompt_template' in x]
chat_models = [x for x in models if 'chat_template' in x]
embedding_models = [x for x in models if 'chat_template' not in x and 'prompt_template' not in x]

rendered_template = template.render(completion_models=completion_models, chat_models=chat_models, embedding_models=embedding_models)

with open("README.md", "w") as f:
    f.write(rendered_template)
print("README.md generated")
