import datetime

# Function to get the date in the format "DD/MM/YY"
def get_formatted_date(date):
    return date.strftime("%d/%m/%y")

# Function to calculate the total expenses for a given expense list
def calculate_expenses(expenses):
    total_expenses = 0

    for expense in expenses:
        # Calculate the number of occurrences in the month
        occurrences = (end_date - expense['start_date']).days // expense['interval'] + 1
        total_expenses += occurrences * expense['amount']

    return total_expenses

# Function to calculate the total savings for a given savings goal list
def calculate_savings(saving_goals, income):
    total_savings = 0

    for goal in saving_goals:
        if goal['percentage']:
            goal_amount = income * goal['amount'] / 100
        else:
            goal_amount = goal['amount']
        
        total_savings += goal_amount

    return total_savings

# Function to validate a date string in the format "DD/MM/YY"
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d/%m/%y")
        return True
    except ValueError:
        return False

# Function to validate a numeric input
def validate_numeric_input(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Get current date
current_date = datetime.datetime.now().date()

# Get income from the user
while True:
    income_str = input("Enter your income for the month: $")
    if validate_numeric_input(income_str):
        income = float(income_str)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

# Get expenses information
while True:
    num_expenses_str = input("Enter the number of expenses: ")
    if num_expenses_str.isdigit():
        num_expenses = int(num_expenses_str)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

expenses = []

for i in range(num_expenses):
    print(f"\nExpense {i+1}:")
    name = input("Enter the name of the expense: ")

    while True:
        interval_str = input("Enter how often this expense occurs (in days): ")
        if interval_str.isdigit():
            interval = int(interval_str)
            break
        else:
            print("Invalid input. Please enter a positive integer.")

    while True:
        start_date_str = input("Enter the next date of this expense (in the format DD/MM/YY): ")
        if validate_date(start_date_str):
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%y").date()
            break
        else:
            print("Invalid input. Please enter a valid date in the format DD/MM/YY.")

    while True:
        amount_str = input("Enter the amount of the expense: $")
        if validate_numeric_input(amount_str):
            amount = float(amount_str)
            break
        else:
            print("Invalid input. Please enter a numeric value.")

    expenses.append({
        'name': name,
        'interval': interval,
        'start_date': start_date,
        'amount': amount
    })

# Get saving goals information
while True:
    num_goals_str = input("\nEnter the number of saving goals: ")
    if num_goals_str.isdigit():
        num_goals = int(num_goals_str)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

saving_goals = []

for i in range(num_goals):
    print(f"\nSavings Goal {i+1}:")
    name = input("Enter the name of the savings goal: ")
    goal_type = input("Enter the goal type (percentage or amount): ")

    if goal_type.lower() == "percentage":
        while True:
            amount_str = input("Enter the percentage of income to save (%): ")
            if validate_numeric_input(amount_str):
                amount = float(amount_str)
                break
            else:
                print("Invalid input. Please enter a numeric value.")
                
        saving_goals.append({
            'name': name,
            'percentage': True,
            'amount': amount
        })
    else:
        while True:
            amount_str = input("Enter the amount to save for the month: $")
            if validate_numeric_input(amount_str):
                amount = float(amount_str)
                break
            else:
                print("Invalid input. Please enter a numeric value.")
                
        saving_goals.append({
            'name': name,
            'percentage': False,
            'amount': amount
        })

# Calculate the end date (next month on the same day as the current date)
end_date = current_date.replace(month=current_date.month + 1)

# Calculate total expenses and savings
total_expenses = calculate_expenses(expenses)
total_savings = calculate_savings(saving_goals, income)

# Display the budget summary
print("\n--- Budget Summary ---")
print("Current Date:", get_formatted_date(current_date))
print("Next Month End Date:", get_formatted_date(end_date))
print("Income: $", income)
print("Total Expenses: $", total_expenses)

# Print expense details
print("\nExpense Details:")
for expense in expenses:
    occurrences = (end_date - expense['start_date']).days // expense['interval'] + 1
    expense_total = occurrences * expense['amount']
    print(f"{expense['name']}: ${expense_total}")

# Print saving goal details
print("Total Savings: $", total_savings)
print("\nSaving Goal Details:")
for goal in saving_goals:
    if goal['percentage']:
        goal_amount = income * goal['amount'] / 100
    else:
        goal_amount = goal['amount']
    print(f"{goal['name']}: ${goal_amount}")

print("Remaining Amount: $", income - total_expenses - total_savings)
