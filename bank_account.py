class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            return self.balance

    def display_balance(self):
        return f"Account owner: {self.owner}, Balance: ${self.balance:.2f}"

