def main():
  """
  This function prompts the user for a task, its priority, and time sensitivity,
  then provides a customized reminder using conditional statements and loops.
  """
  # Prompt for task and store it
  task = input("Enter your task: ")

  # Prompt for priority and store it with case-insensitive conversion
  priority = input("Priority (high/medium/low): ").lower()

  # Prompt for time sensitivity and store it with case-insensitive conversion
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Use match case for priority levels
  match priority:
    case "high":
      reminder_prefix = "**High priority!**"
    case "medium":
      reminder_prefix = "**Medium priority.**"
    case "low":
      reminder_prefix = "**Low priority.**"
    case _:
      print("Invalid priority level. Please enter high, medium, or low.")
      return  # Exit the function if invalid priority

  # Modify reminder based on time sensitivity (using an if statement)
  if time_bound == "yes":
    reminder_suffix = " This requires immediate attention today!"
  else:
    reminder_suffix = " Consider completing it when you have free time."

  # Print the complete reminder
  print(f"\nReminder: '{task}' is a {reminder_prefix}{reminder_suffix}")
  print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
  print(" Click here to tweet! ")

if __name__ == "__main__":
  main()
