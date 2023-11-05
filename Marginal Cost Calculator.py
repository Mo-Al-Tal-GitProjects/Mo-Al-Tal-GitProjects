import json

def calculate_marginal_cost(previous_total_cost, current_total_cost, previous_quantity, current_quantity):
    return (current_total_cost - previous_total_cost) / (current_quantity - previous_quantity)

def save_calculation(product_name, current_total_cost, current_quantity, marginal_cost, calculations):
    calculations[product_name] = {
        "Total Cost": current_total_cost,
        "Quantity Produced": current_quantity,
        "Marginal Cost": marginal_cost
    }
    with open("marginal_cost_calculations.json", "w") as file:
        json.dump(calculations, file)

def main():
    print("Marginal Cost Calculator")

    calculations = retrieve_saved_calculations()

    previous_total_cost = 0
    previous_quantity = 0

    while True:
        print("Options:")
        print("1. Calculate Marginal Cost")
        print("2. Retrieve Saved Calculations")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            product_name = input("Enter product name: ")
            current_total_cost = float(input("Enter current total cost: "))
            current_quantity = float(input("Enter current quantity produced: "))

            if previous_total_cost == 0:
                marginal_cost = 0
            else:
                marginal_cost = calculate_marginal_cost(previous_total_cost, current_total_cost, previous_quantity, current_quantity)

            print(f"Marginal Cost for {product_name}: {marginal_cost}")

            save_calculation(product_name, current_total_cost, current_quantity, marginal_cost, calculations)

            previous_total_cost = current_total_cost
            previous_quantity = current_quantity

        elif choice == "2":
            if calculations:
                print("Saved Marginal Cost Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Total Cost: {data['Total Cost']}")
                    print(f"Quantity Produced: {data['Quantity Produced']}")
                    print(f"Marginal Cost: {data['Marginal Cost']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")

        elif choice == "3":
            print("Exiting the Marginal Cost Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")



def retrieve_saved_calculations():
    try:
        with open("marginal_cost_calculations.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    main()
