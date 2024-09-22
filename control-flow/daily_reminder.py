# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task."

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

