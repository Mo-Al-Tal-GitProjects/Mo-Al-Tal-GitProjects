import json

def calculate_average_variable_costs(total_variable_costs, total_quantity):
    return total_variable_costs / total_quantity

def save_calculation(product_name, total_variable_costs, total_quantity, average_variable_costs, calculations):
    calculations[product_name] = {
        "Total Variable Costs": total_variable_costs,
        "Total Quantity": total_quantity,
        "Average Variable Costs": average_variable_costs
    }
    with open("average_variable_costs_calculations.json", "w") as file:
        json.dump(calculations, file)

def main():
    print("Average Variable Costs Calculator")

    calculations = retrieve_saved_calculations()

    while True:
        print("Options:")
        print("1. Calculate Average Variable Costs")
        print("2. Retrieve Saved Calculations")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            product_name = input("Enter product name: ")
            total_variable_costs = float(input("Enter total variable costs: "))
            total_quantity = float(input("Enter total quantity produced: "))

            average_variable_costs = calculate_average_variable_costs(total_variable_costs, total_quantity)

            print(f"Average Variable Costs for {product_name}: {average_variable_costs}")

            save_calculation(product_name, total_variable_costs, total_quantity, average_variable_costs, calculations)

        elif choice == "2":
            if calculations:
                print("Saved Average Variable Costs Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Total Variable Costs: {data['Total Variable Costs']}")
                    print(f"Total Quantity: {data['Total Quantity']}")
                    print(f"Average Variable Costs: {data['Average Variable Costs']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")

        elif choice == "3":
            print("Exiting the Average Variable Costs Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

def retrieve_saved_calculations():
    try:
        with open("average_variable_costs_calculations.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    main()

