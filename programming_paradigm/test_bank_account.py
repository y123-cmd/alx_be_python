from bank_account import BankAccount

def test_bank_account():
    account = BankAccount(account_number="123456", account_holder="John Doe")

    # Check deposit
    deposit_result = account.deposit(100)
    print(f"Deposit Result: {deposit_result}")  # Debug print
    assert deposit_result == True
    assert account.display_balance() == "Balance: $100.00"

    # Check withdrawal
    withdraw_result = account.withdraw(50)
    print(f"Withdraw Result: {withdraw_result}")  # Debug print
    assert withdraw_result == True
    assert account.display_balance() == "Balance: $50.00"

    # Check withdrawal more than balance
    assert account.withdraw(100) == "Insufficient funds"

    # Check balance display
    assert account.display_balance() == "Balance: $50.00"

test_bank_account()
print("All tests passed!")

