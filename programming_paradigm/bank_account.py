import os

class BankAccount:
    def __init__(self, initial_balance=0):
        self.file_path = "balance.txt"
        self._account_balance = initial_balance if not os.path.exists(self.file_path) else self.read_balance()

    def read_balance(self):
        with open(self.file_path, 'r') as f:
            return float(f.read().strip())

    def save_balance(self):
        with open(self.file_path, 'w') as f:
            f.write(str(self._account_balance))

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            self.save_balance()  # Save balance after deposit
            print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self._account_balance:
            print("Insufficient funds.")
            return False
        else:
            self._account_balance -= amount
            self.save_balance()  # Save balance after withdrawal
            print(f"Withdrew: ${amount:.1f}")
            return True

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

