# match_case_calculator.py using if-elif-else

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation they'd like to perform
operation = input("Choose the operation (+, -, *, /): ")

# Use if-elif-else to handle different operations
if operation == '+':
    result = num1 + num2
    print(f"The result is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result is {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation. Please choose from +, -, *, or /.")

