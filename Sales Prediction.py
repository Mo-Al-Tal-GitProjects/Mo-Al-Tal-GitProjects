def calculate_profit(projected_sales, profit_margin):
    return projected_sales * profit_margin

def calculate_tax(profit, tax_rate):
    return profit * tax_rate

if __name__ == "__main__":
    print("Sales Prediction and Profit Calculator")
    print("---------------------------------------")

    while True:
        try:
            projected_sales = float(input("Enter projected sales amount: $"))
            profit_margin = float(input("Enter the profit margin (e.g., 0.23 for 23%): "))

            # Calculate profit
            profit = calculate_profit(projected_sales, profit_margin)

            # Calculate tax
            tax_rate = 0.15  # Example tax rate (you can customize this)
            tax = calculate_tax(profit, tax_rate)

            # Display results
            print(f"Estimated Profit: ${profit:.2f}")
            print(f"Tax (15%): ${tax:.2f}")
            print(f"Net Profit: ${profit - tax:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
