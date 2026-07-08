def calculate_salary(hours, price):
    return hours * price


def check_salary(salary):
    if salary >= 1000:
        print("Status: High Salary")
    elif salary >= 500:
        print("Status: Normal Salary")
    else:
        print("Status: Low Salary")


# Take information
name = input("Enter employee name: ")
hours = float(input("Enter working hours: "))
price = float(input("Enter hourly salary: "))

# Calculate salary
result = calculate_salary(hours, price)

# Show result
print("Employee:", name)
print("Salary:", result)

# Check salary
check_salary(result)
