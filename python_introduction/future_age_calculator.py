# Prompt the user to input their current age
current_age = int(input("How old are you? "))

# Calculate the age in 2050
current_year = 2023
future_year = 2050
years_to_add = future_year - current_year
future_age = current_age + years_to_add

# Print the result
print(f"In {future_year}, you will be {future_age} years old.")
