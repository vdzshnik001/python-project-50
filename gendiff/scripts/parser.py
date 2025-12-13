import json
import yaml

def read_file(path: str) -> dict:
    if path.endswith('.json'):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    elif path.endswith(('.yml', '.yaml')):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)
    else:
        raise ValueError('unsupported format')