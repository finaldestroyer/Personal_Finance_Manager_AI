import json
import os
from sklearn.linear_model import LinearRegression
import numpy as np

SAVINGS_FILE = 'savings.json'

def load_savings_data():
    if os.path.exists(SAVINGS_FILE):
        try:
            with open(SAVINGS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading savings data. File may be corrupted.")
            return {"goal": 0, "amount": 0, "history": []}
    return {"goal": 0, "amount": 0, "history": []}

def save_savings_data(data):
    try:
        with open(SAVINGS_FILE, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("Error saving savings data.")

def set_savings_goal(goal):
    try:
        goal = float(goal)
        data = load_savings_data()
        data["goal"] = goal
        save_savings_data(data)
    except ValueError:
        print("Invalid goal amount. Please enter a numeric value.")

def add_savings(amount):
    try:
        amount = float(amount)
        data = load_savings_data()
        data["amount"] += amount
        data["history"].append(amount)
        save_savings_data(data)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_savings():
    return load_savings_data()

def predict_time_to_goal():
    data = load_savings_data()
    goal = data["goal"]
    current_savings = data["amount"]
    
    if len(data["history"]) < 2:
        return "Not enough data to predict savings goal."

    X = np.array(range(1, len(data["history"]) + 1)).reshape(-1, 1)
    y = np.array(data["history"]).cumsum()

    model = LinearRegression()
    model.fit(X, y)

    required_amount = goal - current_savings
    if required_amount <= 0:
        return "Goal already reached!"
    
    prediction = model.predict(np.array([[len(data["history"]) + 1]]))[0]
    predicted_weeks = (goal - current_savings) / (prediction - y[-1]) + len(data["history"])

    return f"At your current savings rate, you'll reach your goal in approximately {int(predicted_weeks)} weeks."
