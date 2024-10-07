# bank_account.py

import os

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
        self.load_balance()

    def load_balance(self):
        if os.path.exists("balance.txt"):
            with open("balance.txt", "r") as f:
                self.account_balance = float(f.read().strip())
                print(f"Loaded balance: ${self.account_balance:.2f}")  # Debugging line

    def save_balance(self):
        with open("balance.txt", "w") as f:
            f.write(str(self.account_balance))
            print(f"Saved balance: ${self.account_balance:.2f}")  # Debugging line

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            self.save_balance()
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            self.save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
