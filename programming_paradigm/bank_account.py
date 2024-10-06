class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}')
            return amount
        return 0

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            print(f'Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}')
            return True

    def display_balance(self):
        print(f'Current Balance: ${self.balance:.2f}')
        return self.balance

