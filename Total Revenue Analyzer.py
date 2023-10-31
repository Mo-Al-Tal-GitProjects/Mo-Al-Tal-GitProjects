import json

def calculate_total_revenue(price, quantity):
    return price * quantity

def save_calculation(product_name, price, quantity, total_revenue, calculations):
    calculations[product_name] = {
        "Price": price,
        "Quantity": quantity,
        "Total Revenue": total_revenue
    }
    with open("calculations.json", "w") as file:
        json.dump(calculations, file)

def retrieve_saved_calculations():
    try:
        with open("calculations.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    print("Total Revenue Calculator")
    
    calculations = retrieve_saved_calculations()
    
    while True:
        print("Options:")
        print("1. Calculate Total Revenue")
        print("2. Retrieve Saved Calculations")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            product_name = input("Enter product name: ")
            price = float(input("Enter the price: "))
            quantity = float(input("Enter the quantity in demand: "))
            
            total_revenue = calculate_total_revenue(price, quantity)
            print(f"Total Revenue for {product_name}: {total_revenue}")
            
            save_calculation(product_name, price, quantity, total_revenue, calculations)
        
        elif choice == "2":
            if calculations:
                print("Saved Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Price: {data['Price']}")
                    print(f"Quantity: {data['Quantity']}")
                    print(f"Total Revenue: {data['Total Revenue']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")
        
        elif choice == "3":
            print("Exiting the Total Revenue Calculator.")
            break
        
        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

if __name__ == "__main__":
    main()
