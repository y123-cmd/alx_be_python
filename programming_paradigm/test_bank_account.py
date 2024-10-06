from bank_account import BankAccount  # Ensure this line is present

def test_bank_account():
    account = BankAccount('123456', 'John Doe')
    
    # Test deposit
    assert account.deposit(100) == True
    assert account.display_balance() == 100.0  # This should now pass
    
    # Test withdrawal
    assert account.withdraw(50) == True
    assert account.display_balance() == 50.0

    # Test insufficient funds
    assert account.withdraw(100) == False
    assert account.display_balance() == 50.0

    print("All tests passed!")

if __name__ == "__main__":
    test_bank_account()

