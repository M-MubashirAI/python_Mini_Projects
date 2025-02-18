# Expense Tracker (JSON & Dictionaries) 💰

## 📌 Description
This Expense Tracker is a simple Python program that helps users record, categorize, and manage their daily expenses. The data is stored in a JSON file, ensuring that expenses are saved even after the program is closed.

## 🚀 Features
- ✅ Add an expense (Category, Amount, Date)
- ✅ View total expenses
- ✅ Filter expenses by category
- ✅ Data stored in `expenses.json` file (persistent storage)

## 🛠️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/M-MubashirAI/Python-Mini-Projects.git
    cd Python-Mini-Projects/Expense-Tracker
    ```

2. Ensure Python is installed (Python 3.x recommended).

3. Run the program:
    ```bash
    python expense_tracker.py
    ```

## 📜 Usage
1. Run the script:
    ```bash
    python expense_tracker.py
    ```

2. Follow on-screen instructions:
    - Enter a category (e.g., Food, Travel, Shopping)
    - Enter the amount spent
    - Enter the date (YYYY-MM-DD format)
    - View or filter expenses

## 🔹 Example Output

## 📌 JSON File Example (`expenses.json`)
```json
{
    "expenses": [
        {"category": "Food", "amount": 250.50, "date": "2025-02-16"},
        {"category": "Transport", "amount": 100.00, "date": "2025-02-15"}
    ]
}

