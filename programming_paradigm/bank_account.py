class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Initialize account_balance attribute

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.account_balance:.2f}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}. New Balance: ${self.account_balance:.2f}")
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        return self.account_balance

