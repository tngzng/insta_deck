import os
import json

config = {}


ENV_FILE = "env.json"
if os.path.isfile(ENV_FILE):
    with open(ENV_FILE) as f:
        env_vars = json.load(f)

    for var_name, val in env_vars.items():
        config[var_name] = val
