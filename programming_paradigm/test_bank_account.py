# test_bank_account.py

from bank_account import BankAccount  # Import the BankAccount class

def test_bank_account():
    account = BankAccount('123456', 'John Doe')

    # Test deposit
    deposit_result = account.deposit(100)
    assert deposit_result == True
    assert account.display_balance() == 100.0

    # Test withdrawal
    withdraw_result = account.withdraw(50)
    assert withdraw_result == True
    assert account.display_balance() == 50.0

    # Test insufficient funds
    withdraw_result = account.withdraw(100)
    assert withdraw_result == False
    assert account.display_balance() == 50.0

    print("All tests passed!")

if __name__ == "__main__":
    test_bank_account()

