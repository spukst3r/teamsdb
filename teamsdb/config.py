import os

import yaml


db = {
    'user': 'teamsdb',
    'password': '1q2w3e',
    'name': 'teamsdb',
    'host': os.environ.get('DB_HOST'),
}

app = {
    'port': 8080,
}

default = {
    'db': db,
    'app': app,
}


def load_config(filename):
    if not filename:
        return default

    with open(filename) as f:
        config_file = yaml.load(f)

    return {
        'db': {**db, **config_file.get('db')},
        'app': {**app, **config_file.get('app')},
    }
