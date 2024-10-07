# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount:.1f}"  # Return the message instead of printing it

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.1f}"  # Return the message instead of printing it
        else:
            return "Insufficient funds."  # Return the message instead of printing it

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"  # Return the balance instead of printing it

