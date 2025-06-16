import os
import json
from datetime import datetime

SAVE_DIR = "chats"
os.makedirs(SAVE_DIR, exist_ok = True)


def save_chat(history, filename = None):
    if not filename:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'chat_{timestamp}.json'

    path = os.path.join(SAVE_DIR, filename)

    with open(path, 'w', encoding = 'utf-8') as f:
        json.dump(history, f, ensure_ascii = False, indent = 2)

    return filename


def list_saved_chats():
    return [f for f in os.listdir(SAVE_DIR) if f.endswith('.json')]


def load_chat(filename):
    path = os.path.join(SAVE_DIR, filename)

    if os.path.exists(path):
        with open(path, 'r', encoding = 'utf-8') as f:
            return json.load(f)

    return []
