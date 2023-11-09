import json

def calculate_total_cost(fixed_costs, variable_costs):
    return fixed_costs + variable_costs

def save_calculation(product_name, fixed_costs, variable_costs, total_cost, calculations):
    calculations[product_name] = {
        "Fixed Costs": fixed_costs,
        "Variable Costs": variable_costs,
        "Total Cost": total_cost
    }
    with open("total_cost_calculations.json", "w") as file:
        json.dump(calculations, file)

def main():
    print("Total Cost Calculator")

    calculations = retrieve_saved_calculations()

    while True:
        print("Options:")
        print("1. Calculate Total Cost")
        print("2. Retrieve Saved Calculations")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            product_name = input("Enter product name: ")
            fixed_costs = float(input("Enter total fixed costs: "))
            variable_costs = float(input("Enter total variable costs: "))

            total_cost = calculate_total_cost(fixed_costs, variable_costs)
            print(f"Total Cost for {product_name}: {total_cost}")

            save_calculation(product_name, fixed_costs, variable_costs, total_cost, calculations)
        elif choice == "2":
            if calculations:
                print("Saved Total Cost Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Fixed Costs: {data['Fixed Costs']}")
                    print(f"Variable Costs: {data['Variable Costs']}")
                    print(f"Total Cost: {data['Total Cost']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")

        elif choice == "3":
            print("Exiting the Total Cost Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

def retrieve_saved_calculations():
    try:
        with open("total_cost_calculations.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
if __name__ == "__main__":
    main()
