import os
from arithmetic_operations import perform_operation

def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return False
    if os.path.getsize(file_path) == 0:
        print(f"Error: {file_path} is empty.")
        return False
    return True

def main():
    # Check if arithmetic_operations.py exists and is not empty
    if not check_file('arithmetic_operations.py'):
        return

    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

