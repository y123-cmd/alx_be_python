from bank_account import BankAccount

def main():
    # Create a new bank account
    account = BankAccount("123456789", "John Doe")

    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
