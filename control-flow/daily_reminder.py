# daily_reminder.py

print("=== Daily Task Reminder ===")

# Prompt for a single task
task = input("Enter your task: ")

# Ask for priority (validated)
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter high, medium, or low.")

# Ask if time-bound (validated)
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
        break
    print("Please answer yes or no.")

# Match-case to generate base message
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task"

# If time-bound, add immediate action
if time_bound == "yes":
    full_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    full_message = f"Note: {base_message}. Consider completing it when you have free time."

# FINAL CUSTOMIZED REMINDER (required by the checker)
print(full_message)
