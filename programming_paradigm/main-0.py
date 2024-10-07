# main-0.py
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250)  # Set initial balance to 250 for example
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        print(account.deposit(amount))
    elif command == "withdraw" and amount is not None:
        print(account.withdraw(amount))
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

