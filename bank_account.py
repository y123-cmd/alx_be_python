# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Use a leading underscore for encapsulation

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds are available."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False  # Return False if insufficient funds or invalid amount

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
