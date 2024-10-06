from bank_account import BankAccount

def test_bank_account():
    account = BankAccount('123456', 'John Doe')  # Pass required arguments
    assert account.deposit(100) == True
    assert account.withdraw(50) == True
    assert account.balance == 50
    assert account.withdraw(100) == False  # Attempt to withdraw more than available
    assert account.balance == 50
    account.display_balance()  # Check balance display

if __name__ == "__main__":
    test_bank_account()
    print("All tests passed!")

