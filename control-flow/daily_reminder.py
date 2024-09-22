# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on priority
if priority == 'high':
    reminder = f"'{task}' is a high priority task."
    if time_bound == 'yes':
        reminder += " It requires immediate attention today!"
elif priority == 'medium':
    reminder = f"'{task}' is a medium priority task."
    if time_bound == 'yes':
        reminder += " Consider addressing it soon."
else:  # low priority
    reminder = f"'{task}' is a low priority task."
    if time_bound == 'yes':
        reminder += " You may want to consider it when you have time."

print(reminder)

