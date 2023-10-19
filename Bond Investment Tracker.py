# Bond Investment Tracker

# Define an empty list to store bond purchase records
bond_investments = []

# Function to add a bond purchase record
def add_bond_investment():
    bond_name = input("Enter the name of the bond: ")
    purchase_date = input("Enter the purchase date (YYYY-MM-DD): ")
    face_value = float(input("Enter the face value of the bond: "))
    purchase_price = float(input("Enter the purchase price: "))
    coupon_rate = float(input("Enter the annual coupon rate (%): "))
    years_to_maturity = int(input("Enter the years to maturity: "))
    
    bond_record = {
        "Bond Name": bond_name,
        "Purchase Date": purchase_date,
        "Face Value": face_value,
        "Purchase Price": purchase_price,
        "Coupon Rate": coupon_rate,
        "Years to Maturity": years_to_maturity
    }
    
    bond_investments.append(bond_record)
    print("Bond investment added successfully.")

# Function to display all bond purchase records
def display_bond_investments():
    print("\nBond Investment Records:")
    for idx, bond in enumerate(bond_investments, start=1):
        print(f"Bond #{idx}")
        for key, value in bond.items():
            print(f"{key}: {value}")
        print()

# Function to calculate the yield to maturity (YTM) for a bond
def calculate_ytm(face_value, purchase_price, coupon_rate, years_to_maturity):
    # Add YTM calculation logic here
    pass

# Function to calculate the total value of bond investments
def calculate_total_investment_value():
    total_value = sum(bond['Purchase Price'] for bond in bond_investments)
    print(f"Total Value of Bond Investments: ${total_value:.2f}")

# Main menu for the bond investment tracker
while True:
    print("\nBond Investment Tracker")
    print("1. Add Bond Investment")
    print("2. Display Bond Investments")
    print("3. Calculate YTM for a Bond")
    print("4. Calculate Total Investment Value")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_bond_investment()
    elif choice == "2":
        display_bond_investments()
    elif choice == "3":
        # Implement YTM calculation
        pass
    elif choice == "4":
        calculate_total_investment_value()
    elif choice == "5":
        print("Exiting Bond Investment Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
