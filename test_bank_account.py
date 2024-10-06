from bank_account import BankAccount  # Import the BankAccount class

def test_bank_account():
    account = BankAccount()

    # Check deposit
    assert account.deposit(100) == True
    assert account.display_balance() == "Balance: $100.00"

    # Check withdrawal
    assert account.withdraw(50) == True
    assert account.display_balance() == "Balance: $50.00"

    # Check withdrawal more than balance
    assert account.withdraw(100) == "Insufficient funds"

    # Check balance display
    assert account.display_balance() == "Balance: $50.00"

test_bank_account()
print("All tests passed!")
