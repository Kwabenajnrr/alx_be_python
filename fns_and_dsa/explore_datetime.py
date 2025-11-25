import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)




def calculate_future_date():
    days = int(input("Enter number of days to add: "))
    current_date = datetime.date.today()
    
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    
    print("Future Date:", formatted_future)



display_current_datetime()
calculate_future_date()
