from arithmetic_operations import perform_operation

def main():
    try:
        # Prompting user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

        # Call the function and get the result
        result = perform_operation(num1, num2, operation)

        # Display the result
        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

