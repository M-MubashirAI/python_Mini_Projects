import json
import os

# JSON file to store expenses
FILE_NAME = "expenses.json"

# Function to load expenses from JSON file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"expenses": []}

# Function to save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense():
    category = input("Enter expense category: ").capitalize()
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    expenses = load_expenses()
    expenses["expenses"].append({"category": category, "amount": amount, "date": date})
    
    save_expenses(expenses)
    print("✅ Expense added successfully!\n")

# Function to view total expenses
def view_total_expenses():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses["expenses"])
    print(f"💰 Total Expenses: {total}\n")

# Function to filter expenses by category
def filter_expenses():
    category = input("Enter category to filter: ").capitalize()
    expenses = load_expenses()
    
    filtered = [exp for exp in expenses["expenses"] if exp["category"] == category]

    if filtered:
        print(f"\n📂 Expenses in '{category}':")
        for exp in filtered:
            print(f"- {exp['date']}: {exp['amount']}")
    else:
        print("❌ No expenses found in this category.")
    print()

# Main function (Menu)
def main():
    while True:
        print("\n📌 Expense Tracker Menu:")
        print("1️⃣ Add Expense")
        print("2️⃣ View Total Expenses")
        print("3️⃣ Filter Expenses by Category")
        print("4️⃣ Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            print("🚀 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
