ask1 = "Finish project report"
ask2 = "Read a book"

description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

if description == ask1 and priority == "high" and time == "yes":
    print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")

if description == ask2  and priority == "low" and time == "no":
    print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
