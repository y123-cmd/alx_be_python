class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}")
            return True

    def display_balance(self):
        print(f"Current Balance: {self.balance:.2f}")  # Correctly format the output
        return self.balance  # Returning the balance if needed

