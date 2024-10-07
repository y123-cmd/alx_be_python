# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    while True:
        command = input("Enter command (deposit:amount, withdraw:amount, display, or exit): ")
        if command.lower() == 'exit':
            break
        
        parts = command.split(':')
        cmd = parts[0]
        amount = float(parts[1]) if len(parts) > 1 else None

        if cmd == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif cmd == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif cmd == "display":
            account.display_balance()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

