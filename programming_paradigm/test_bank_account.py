from bank_account import BankAccount  # Ensure you import the BankAccount class

def test_bank_account():
    # Create an instance of BankAccount
    account = BankAccount('123456', 'John Doe')
    
    # Test deposit
    deposit_result = account.deposit(100)
    print(f"Deposit Result: {deposit_result}")
    assert deposit_result == True  # Check if deposit returns True
    assert account.display_balance() == 100  # Check if balance is correct

    # Test withdrawal
    withdrawal_result = account.withdraw(50)
    print(f"Withdraw Result: {withdrawal_result}")
    assert withdrawal_result == True  # Check if withdrawal returns True
    assert account.display_balance() == 50  # Check if balance is correct after withdrawal

    # Test withdrawing more than balance
    withdrawal_result = account.withdraw(100)
    print(f"Withdraw Result: {withdrawal_result}")  # Expect this to fail
    assert withdrawal_result == False  # Check if withdrawal returns False
    assert account.display_balance() == 50  # Balance should still be 50

    # Check display balance
    current_balance = account.display_balance()
    print(f"Current Balance: {current_balance}")
    assert current_balance == 50  # Check if display balance is correct

if __name__ == "__main__":
    test_bank_account()

