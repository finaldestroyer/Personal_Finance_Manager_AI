import json
import os

BUDGET_FILE = 'budget.json'

def load_budget_data():
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading budget data. File may be corrupted.")
            return {}
    return {}

def save_budget_data(data):
    try:
        with open(BUDGET_FILE, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("Error saving budget data.")

def set_budget(category, amount):
    data = load_budget_data()
    data[category] = amount
    save_budget_data(data)

def view_budget():
    return load_budget_data()
