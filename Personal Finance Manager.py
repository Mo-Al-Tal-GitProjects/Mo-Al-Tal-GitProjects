def calculate_tax(income, deductions):
    # Define tax brackets and rates
    tax_brackets = [
        (0, 10000, 0.10),
        (10001, 50000, 0.20),
        (50001, 100000, 0.30),
        (100001, float('inf'), 0.40)
    ]

    # Calculate taxable income after deductions
    taxable_income = max(income - deductions, 0)

    # Calculate tax based on tax brackets
    tax = 0
    for bracket in tax_brackets:
        min_income, max_income, rate = bracket
        if taxable_income <= 0:
            break
        if taxable_income <= max_income:
            tax += taxable_income * rate
            break
        else:
            tax += (max_income - min_income + 1) * rate
            taxable_income -= (max_income - min_income + 1)

    return tax

def budget_planner(income, expenses):
    # Calculate available income after expenses
    available_income = income - sum(expenses)

    return available_income

def main():
    # Get user input
    income = float(input("Enter your monthly income: "))
    deductions = float(input("Enter your monthly deductions (e.g., taxes, insurance): "))
    
    # Get user input for monthly expenses
    num_expenses = int(input("Enter the number of monthly expenses: "))

    # Check if the number of expenses is reasonable (e.g., less than 100)
    if num_expenses <= 0 or num_expenses > 100:
        print("Please enter a reasonable number of expenses.")
    else:
        expenses = []
        for i in range(num_expenses):
            expense = float(input(f"Enter expense {i + 1}: "))
            expenses.append(expense)

        # Calculate income tax
        tax = calculate_tax(income, deductions)

        # Calculate available income after expenses
        available_income = budget_planner(income, expenses)

        # Create a formatted table
        table = f"{'Description':<20}{'Amount ($)':<15}\n"
        table += "-" * 35 + "\n"
        table += f"Income{'':<12}${income:<11,.2f}\n"
        table += f"Deductions{'':<12}${deductions:<11,.2f}\n"
        table += f"Income Tax{'':<12}${tax:<11,.2f}\n"
        table += f"Total Expenses{'':<12}${sum(expenses):<11,.2f}\n"
        table += f"Available Income{'':<12}${available_income:<11,.2f}"

        # Print the table
        print("\nPersonal Finance Summary")
        print(table)

if __name__ == "__main__":
    main()

