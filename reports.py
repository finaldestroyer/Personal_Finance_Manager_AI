def view_income_report(data):
    if not data:
        print("No income data available.")
    else:
        print("\nIncome Report:")
        for entry in data:
            print(f"Source: {entry['source']}, Amount: {entry['amount']}")

def view_expense_report(data):
    if not data:
        print("No expense data available.")
    else:
        print("\nExpense Report:")
        for entry in data:
            print(f"Category: {entry['category']}, Description: {entry['description']}, Amount: {entry['amount']}")

def view_budget_report(data):
    if not data:
        print("No budget data available.")
    else:
        print("\nBudget Report:")
        for category, amount in data.items():
            print(f"Category: {category}, Amount: {amount}")

def view_savings_report(data):
    if not data:
        print("No savings data available.")
    else:
        print(f"\nSavings Report:")
        print(f"Current Savings: {data['amount']}")
        print(f"Goal: {data['goal']}")
        print(f"History: {data['history']}")
