import json

def calculate_average_total_cost(total_costs, total_quantity):
    return total_costs / total_quantity

def save_calculation(product_name, total_costs, total_quantity, average_total_cost, calculations):
    calculations[product_name] = {
        "Total Costs": total_costs,
        "Total Quantity": total_quantity,
        "Average Total Cost": average_total_cost
    }
    with open("average_total_cost_calculations.json", "w") as file:
        json.dump(calculations, file)

def main():
    print("Average Total Cost Calculator")

    calculations = retrieve_saved_calculations()

    while True:
        print("Options:")
        print("1. Calculate Average Total Cost")
        print("2. Retrieve Saved Calculations")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            product_name = input("Enter product name: ")
            total_costs = float(input("Enter total costs: "))
            total_quantity = float(input("Enter total quantity produced: "))

            average_total_cost = calculate_average_total_cost(total_costs, total_quantity)

            print(f"Average Total Cost for {product_name}: {average_total_cost}")

            save_calculation(product_name, total_costs, total_quantity, average_total_cost, calculations)

        elif choice == "2":
            if calculations:
                print("Saved Average Total Cost Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Total Costs: {data['Total Costs']}")
                    print(f"Total Quantity: {data['Total Quantity']}")
                    print(f"Average Total Cost: {data['Average Total Cost']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")

        elif choice == "3":
            print("Exiting the Average Total Cost Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

def retrieve_saved_calculations():
    try:
        with open("average_total_cost_calculations.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    main()
