# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task."

# Match Case for priority
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task."
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task."
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Reminder: Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

