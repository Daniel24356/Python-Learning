
import json
import os

DATA_DIR = '.'

def load_data(filename):
    path = os.path.join(DATA_DIR, f'{filename}.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    path = os.path.join(DATA_DIR, f'{filename}.json')
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)