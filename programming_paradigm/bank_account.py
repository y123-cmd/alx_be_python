class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  # Initial balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def check_balance(self):
        """Check the current balance."""
        print(f"Account Balance: ${self.balance:.2f}")

# Example usage (can be moved to main-0.py)
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe")
    account.deposit(100.0)
    account.withdraw(30.0)
    account.check_balance()
