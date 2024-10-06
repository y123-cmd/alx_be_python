from bank_account import BankAccount  # Ensure you're importing the class

def test_bank_account():
    account = BankAccount('123456', 'John Doe')

    assert account.deposit(100) == True  # Test deposit
    assert account.withdraw(50) == True  # Test withdrawal
    assert account.withdraw(100) == False  # Test withdrawing more than balance
    assert account.display_balance() == 50.0  # Check balance

if __name__ == "__main__":
    test_bank_account()
    print("All tests passed!")

