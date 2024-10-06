class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
            return True
        return False

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        elif amount <= 0:
            return "Invalid withdrawal amount"
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}")
            return True

    def display_balance(self):
        return f"Balance: ${self.balance:.2f}"

