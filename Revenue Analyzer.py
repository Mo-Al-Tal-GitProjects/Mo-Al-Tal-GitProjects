import json

def calculate_total_revenue(price, quantity):
    return price * quantity

def calculate_marginal_revenue(prev_total_revenue, new_total_revenue, prev_quantity, new_quantity):
    return (new_total_revenue - prev_total_revenue) / (new_quantity - prev_quantity)

def save_calculation(product_name, price, quantity, total_revenue, marginal_revenue, calculations):
    calculations[product_name] = {
        "Price": price,
        "Quantity": quantity,
        "Total Revenue": total_revenue,
        "Marginal Revenue": marginal_revenue
    }
    with open("calculations.json", "w") as file:
        json.dump(calculations, file)

def main():
    print("Revenue Calculator")
    
    calculations = retrieve_saved_calculations()
    
    while True:
        print("Options:")
        print("1. Calculate Total Revenue")
        print("2. Calculate Marginal Revenue")
        print("3. Retrieve Saved Calculations")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            product_name = input("Enter product name: ")
            price = float(input("Enter the price: "))
            quantity = float(input("Enter the quantity in demand: ")
            
            total_revenue = calculate_total_revenue(price, quantity)
            print(f"Total Revenue for {product_name}: {total_revenue}")
            
            save_calculation(product_name, price, quantity, total_revenue, None, calculations)
        
        elif choice == "2":
            product_name = input("Enter product name: ")
            if product_name in calculations:
                prev_quantity = calculations[product_name]["Quantity"]
                prev_total_revenue = calculations[product_name]["Total Revenue"]
                
                new_quantity = float(input("Enter the new quantity in demand: "))
                new_total_revenue = calculate_total_revenue(calculations[product_name]["Price"], new_quantity)
                
                marginal_revenue = calculate_marginal_revenue(prev_total_revenue, new_total_revenue, prev_quantity, new_quantity)
                print(f"Marginal Revenue for {product_name}: {marginal_revenue}")
                
                save_calculation(product_name, calculations[product_name]["Price"], new_quantity, new_total_revenue, marginal_revenue, calculations)
            else:
                print(f"No data found for {product_name}. Calculate Total Revenue first.")
        
        elif choice == "3":
            if calculations:
                print("Saved Calculations:")
                for product, data in calculations.items():
                    print(f"Product: {product}")
                    print(f"Price: {data['Price']}")
                    print(f"Quantity: {data['Quantity']}")
                    print(f"Total Revenue: {data['Total Revenue']}")
                    if data['Marginal Revenue'] is not None:
                        print(f"Marginal Revenue: {data['Marginal Revenue']}")
                    print("------------------------")
            else:
                print("No saved calculations found.")
        
        elif choice == "4":
            print("Exiting the Revenue Calculator.")
            break
        
        else:
            print("Invalid option. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
