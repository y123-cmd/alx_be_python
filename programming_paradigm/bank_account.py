class BankAccount:
    def __init__(self, initial_balance=0, balance_file="balance.txt"):
        self.balance_file = balance_file
        self.account_balance = self.load_balance(initial_balance)

    def load_balance(self, initial_balance):
        try:
            with open(self.balance_file, 'r') as file:
                return float(file.read())
        except FileNotFoundError:
            return initial_balance

    def save_balance(self):
        with open(self.balance_file, 'w') as file:
            file.write(str(self.account_balance))

    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

