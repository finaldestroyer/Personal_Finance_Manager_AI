import json
import os

INCOME_FILE = 'income.json'

def load_income_data():
    if os.path.exists(INCOME_FILE):
        try:
            with open(INCOME_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading income data. File may be corrupted.")
            return []
    return []

def save_income_data(data):
    try:
        with open(INCOME_FILE, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("Error saving income data.")

def add_income(source, amount):
    data = load_income_data()
    data.append({"source": source, "amount": amount})
    save_income_data(data)

def view_income():
    return load_income_data()
