from bank_account import BankAccount

def test_initialization():
    account = BankAccount("Yvonne", 100)
    assert account.owner == "Yvonne"
    assert account.balance == 100

def test_deposit():
    account = BankAccount("Yvonne", 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = BankAccount("Yvonne", 100)
    account.withdraw(50)
    assert account.balance == 50

def test_display_balance():
    account = BankAccount("Yvonne", 100)
    assert account.display_balance() == "Account owner: Yvonne, Balance: $100.00"

def test_withdraw_insufficient_funds():
    account = BankAccount("Yvonne", 100)
    try:
        account.withdraw(200)
    except ValueError as e:
        assert str(e) == "Insufficient funds"

def run_tests():
    test_initialization()
    test_deposit()
    test_withdraw()
    test_display_balance()
    test_withdraw_insufficient_funds()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()

