# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    
    # Prompt for the priority level and convert it to lowercase for uniformity
    priority = input("Priority (high/medium/low): ").lower()
    
    # Prompt for whether the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder_message = ""

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            reminder_message = f"'{task}' is a high priority task"
        case "medium":
            reminder_message = f"'{task}' is a medium priority task"
        case "low":
            reminder_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return  # Exit if invalid input

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder_message += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder_message += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return  # Exit if invalid input

    # Provide the customized reminder
    print(reminder_message)

if __name__ == "__main__":
    main()
