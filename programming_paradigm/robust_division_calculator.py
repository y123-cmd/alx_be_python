# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)  # Convert numerator to float
        denom = float(denominator)  # Convert denominator to float
        return f"The result of the division is {num / denom:.1f}"  # Format result to one decimal place
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


