import json

def read_storage_config(config_file):
    with open(config_file) as f:
        config = json.load(f)
    return config['storage_connection_string'], config['container_name']