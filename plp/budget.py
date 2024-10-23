print("Welcome to your budget estimator app")

# Gather income details
income = float(input("Enter your monthly post-tax income ($USD): "))
additional = float(input("Enter your additional income expected for next month ($USD): "))

# Calculate total income
total_income = income + additional
print(f"Great! Your total income for next month is ${total_income:.2f}")
print("Now we will get some expenses data...")

def gather_expenses():
    """
    Gather and calculate the user's total expenses.
    Returns:
        float: The total expenses for the month.
    """
    housing = float(input("Enter your monthly housing expense ($USD): "))
    utilities = float(input("Enter your monthly utilities total expenses ($USD): "))
    food = float(input("Enter your monthly food expenses ($USD): "))
    misc = float(input("Enter any additional monthly expenses ($USD): "))
    
    # Calculate total expenses
    total_expenses = housing + utilities + food + misc
    return total_expenses

# Gather and calculate total expenses
expense_total = gather_expenses()
print(f"Great! Your total expenses for next month are ${expense_total:.2f}")

# Calculate the remaining margin
margin = total_income - expense_total

# Display the result
if margin >= 0:
    print(f"Awesome! You have a positive balance of ${margin:.2f} for next month.")
else:
    print(f"Warning! You will be ${-margin:.2f} short next month. Consider adjusting your expenses.")

print("Thank you for using the monthly budget tool!")
