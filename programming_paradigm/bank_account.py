# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

