import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(250.0)  # Starting balance

    def test_withdrawal(self):
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 200.0)  # Ensure balance is updated
        self.account.display_balance()  # Should print "Current Balance: $200.00"

    def test_withdraw_more_than_balance(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 250.0)  # Balance should remain unchanged
        self.account.display_balance()  # Should print "Current Balance: $250.00"

    def test_withdraw_negative_amount(self):
        self.account.withdraw(-50.0)  # Testing withdrawal with negative amount
        self.assertEqual(self.account.balance, 250.0)  # Balance should remain unchanged
        self.account.display_balance()  # Should print "Current Balance: $250.00"

if __name__ == "__main__":
    unittest.main()

