import json

class BankAccount:
    """Represents a bank account with basic functionalities."""
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposit Successful! New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """Withdraws money from the account if sufficient balance exists."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal Successful! Remaining Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance! Transaction failed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def check_balance(self):
        """Returns the current account balance."""
        return f"Account Balance: ${self.balance:.2f}"

    def to_dict(self):
        """Converts account details to a dictionary for JSON storage."""
        return {"name": self.name, "account_number": self.account_number, "balance": self.balance}

class Bank:
    """Manages multiple bank accounts."""
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Loads accounts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return {acc["account_number"]: BankAccount(acc["name"], acc["account_number"], acc["balance"]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_accounts(self):
        """Saves accounts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([acc.to_dict() for acc in self.accounts.values()], file, indent=4)

    def create_account(self, name, account_number, balance=0.0):
        """Creates a new bank account."""
        if account_number in self.accounts:
            print("Account number already exists! Please use a unique number.")
            return
        self.accounts[account_number] = BankAccount(name, account_number, balance)
        self.save_accounts()
        print("Account Created Successfully!")

    def transfer_money(self, from_acc, to_acc, amount):
        """Transfers money between two accounts if sufficient balance exists."""
        if from_acc in self.accounts and to_acc in self.accounts:
            if amount > 0 and self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                self.save_accounts()
                print("Transfer Successful!")
            else:
                print("Insufficient balance or invalid amount!")
        else:
            print("Invalid account numbers! Transfer failed.")

    def get_account(self, account_number):
        """Returns an account object if it exists."""
        return self.accounts.get(account_number, None)

# Main Menu
def main():
    bank = Bank()
    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter Account Holder Name: ")
            acc_num = input("Enter Account Number: ")
            balance = float(input("Enter Initial Deposit (or 0): "))
            bank.create_account(name, acc_num, balance)
        
        elif choice == '2':
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter Amount to Deposit: "))
                account.deposit(amount)
                bank.save_accounts()
            else:
                print("Account not found!")

        elif choice == '3':
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter Amount to Withdraw: "))
                account.withdraw(amount)
                bank.save_accounts()
            else:
                print("Account not found!")

        elif choice == '4':
            acc_num = input("Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                print(account.check_balance())
            else:
                print("Account not found!")

        elif choice == '5':
            from_acc = input("Enter Your Account Number: ")
            to_acc = input("Enter Recipient Account Number: ")
            amount = float(input("Enter Amount to Transfer: "))
            bank.transfer_money(from_acc, to_acc, amount)

        elif choice == '6':
            print("Exiting Banking System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
