from ruamel.yaml import YAML
from pathlib import Path


yaml = YAML(typ="safe")
config = yaml.load(Path("config.yml"))

global_settings = config.pop("global_settings")

import jinja2

for name, settings in config.items():

    with open("template.html", "r") as infile:
        template = jinja2.Template(infile.read())

    with open(f"outputs/{name}.html", 'w') as outfile:
        outfile.write(template.render(
            **global_settings, **settings
        ))
