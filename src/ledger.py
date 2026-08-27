import json
import os

LEDGER_FILE = "parcels.json"


def load_ledger():
    if not os.path.exists(LEDGER_FILE):
        return []
    with open(LEDGER_FILE, "r") as f:
        return json.load(f)


def save_ledger(data):
    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f, indent=2)