import os

class BankAccount:
    def __init__(self):
        self.balance_file = 'balance.txt'
        if not os.path.exists(self.balance_file):
            with open(self.balance_file, 'w') as f:
                f.write('200')  # Initialize with a default balance
        self.load_balance()

    def load_balance(self):
        with open(self.balance_file, 'r') as f:
            self.account_balance = float(f.read().strip())

    def save_balance(self):
        with open(self.balance_file, 'w') as f:
            f.write(f'{self.account_balance:.2f}')

    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance -= amount
        self.save_balance()
        print(f"Withdrew: ${amount:.1f}")
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

