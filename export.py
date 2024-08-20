import pandas as pd
import os
import json

def load_data(file_name):
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error loading data from {file_name}. File may be corrupted.")
            return []
    return []

def export_to_excel():
    income_data = load_data('income.json')
    expenses_data = load_data('expenses.json')
    budget_data = load_data('budget.json')
    savings_data = load_data('savings.json')

    with pd.ExcelWriter('finance_report.xlsx', engine='xlsxwriter') as writer:
        if income_data:
            df_income = pd.DataFrame(income_data)
            df_income.to_excel(writer, sheet_name='Income', index=False)
        
        if expenses_data:
            df_expenses = pd.DataFrame(expenses_data)
            df_expenses.to_excel(writer, sheet_name='Expenses', index=False)
        
        if budget_data:
            df_budget = pd.DataFrame(list(budget_data.items()), columns=['Category', 'Amount'])
            df_budget.to_excel(writer, sheet_name='Budget', index=False)
        
        if savings_data:
            df_savings = pd.DataFrame([savings_data])
            df_savings.to_excel(writer, sheet_name='Savings', index=False)

    for file_name in ['income.json', 'expenses.json', 'budget.json', 'savings.json']:
        if os.path.exists(file_name):
            os.remove(file_name)
