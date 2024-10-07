# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=250.00):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    account = BankAccount()
    account.display_balance()  # Should display $250.00

    # You can also add deposits and withdrawals to test further
    account.deposit(100)        # Add $100
    account.display_balance()    # Should display $350.00

    account.withdraw(50)        # Withdraw $50
    account.display_balance()    # Should display $300.00

    account.withdraw(500)       # Attempt to withdraw more than the balance

