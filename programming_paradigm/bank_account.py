class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

