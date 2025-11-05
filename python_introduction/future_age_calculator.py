def future_age():
    age = int(input("How old are you? "))
    future_year = 2050
    current_year = 2023
    future_age = age + (future_year - current_year)
    return future_age

# Call the function and display the result
result = future_age()
print("In 2050, you will be", result, "years old.")
