class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if funds are sufficient."""
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.1f}")
        return True

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")

