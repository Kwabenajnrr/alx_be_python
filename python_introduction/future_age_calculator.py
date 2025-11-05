def financial():
    monthly_income = int(input("How old are you? "))
    monthly_expenses = int(input("How old are you? "))
    monthly_saving = monthly_income - monthly_expenses

    return monthly_saving

# Call the function and display the result
result = financial()
print("In 2050, you will be", result, "years old.")
