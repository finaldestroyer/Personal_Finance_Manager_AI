import json
import os

EXPENSES_FILE = 'expenses.json'

def load_expenses_data():
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading expenses data. File may be corrupted.")
            return []
    return []

def save_expenses_data(data):
    try:
        with open(EXPENSES_FILE, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("Error saving expenses data.")

def add_expense(category, description, amount):
    data = load_expenses_data()
    data.append({"category": category, "description": description, "amount": amount})
    save_expenses_data(data)

def view_expenses():
    return load_expenses_data()
