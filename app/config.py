import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / 'config' / 'config.yaml'

def load_config(path: CONFIG_PATH):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
