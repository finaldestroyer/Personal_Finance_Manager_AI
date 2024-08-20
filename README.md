# Personal Finance Manager

The Personal Finance Manager is a command-line tool designed to help users manage their personal finances effectively. This tool allows users to track their income, expenses, budget, and savings, with an added feature for predicting the time required to achieve a specified savings goal. Additionally, the tool provides the capability to export financial data into an Excel file for further analysis.

## Features

- **Income Management**: Add and track income records.
- **Expense Management**: Record expenses categorized by type and description. Generate reports detailing all expenses.
- **Budget Management**: Set budget limits for various categories.
- **Savings Management**: Set savings goals, add savings amounts, and view progress.
- **Reports Generation**: Export all financial data to an Excel file for detailed analysis.

## Getting Started

To get started with the Personal Finance Manager, follow these steps:

#### Installation

1. **Clone the Repository**:
   ```bash
    git clone https://github.com/your-username/personal-finance-manager.git
    cd personal-finance-manager

2. **Install Dependencies**:
   ```bash
    "pip install pandas xlsxwriter scikit-learn"

#### Usage

1. **Run the Application**:
    In terminal run "python finance_manager.py"

2. **Interaction with the Menu**:
    - **1: Manage Income**;
    - **2: Manage Expenses**;
    - **3: Manage Budget**;
    - **4: Track Savings**;
    - **5: Generate Reports**;
    - **6: Exit**;


3. **Export to Excel**:
    To generate a report, select the "Generate Reports" option. The data will be exported to personal_finance_report.xlsx.

### File Structure
    data/:                              ####Contains JSON files for income, expenses, budget, and savings data.
    income.py:                          ###Manages income records.
    expenses.py:                        ###Manages expense records.
    budget.py:                          ###Manages budget records.
    savings.py:                         ###Manages savings records.
    reports.py:                         ###Contains functions for generating reports.
    export.py:                          ###Handles exporting data to Excel.
    finance_manager.py:                 ###The main entry point for the application.

### Data Storage

The application uses JSON files to store financial data:
    income.json for income data.
    expenses.json for expense data.
    budget.json for budget data.
    savings.json for savings data.
    These files are cleared after exporting the data to Excel.

### Example:

**Adding Income**
    Choose "Manage Income" from the main menu.
    Enter the source of the income and the amount.
    View the updated income report.

**Predicting Savings Goal Achievement**
    Set a savings goal under "Track Savings."
    Add amounts to your savings regularly.
    Use "Predict Time to Goal" to estimate when you'll reach your savings goal.
