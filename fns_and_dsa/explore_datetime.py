from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Part 1
display_current_datetime()

# Part 2
number_of_days = int(input("Enter number of days to add: "))
calculate_future_date(number_of_days)

