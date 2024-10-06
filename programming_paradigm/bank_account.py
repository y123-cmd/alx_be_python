class BankAccount:
    def __init__(self, account_number, account_holder):
        self.balance = 0
        self.account_number = account_number
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
            return True
        return False

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > 0:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
        return f"Balance: ${self.balance:.2f}"
