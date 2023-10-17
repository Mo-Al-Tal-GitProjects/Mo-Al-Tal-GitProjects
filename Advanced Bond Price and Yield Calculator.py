def calculate_bond_price(par_value, coupon_rate, market_rate, years_to_maturity):
    # Calculate the present value of coupon payments
    coupon_payment = par_value * coupon_rate
    present_value_coupons = 0
    for t in range(1, years_to_maturity + 1):
        present_value_coupons += coupon_payment / (1 + market_rate) ** t

    # Calculate the present value of the face value (par value) at maturity
    present_value_face_value = par_value / (1 + market_rate) ** years_to_maturity

    # Calculate the total bond price
    bond_price = present_value_coupons + present_value_face_value

    return bond_price

def calculate_yield_to_maturity(par_value, coupon_rate, bond_price, years_to_maturity):
    # Define the range of possible market rates for YTM calculation
    lower_rate = 0.01
    upper_rate = 2.0
    ytm = lower_rate

    # Use the bisection method to find the YTM
    while lower_rate < upper_rate:
        ytm = (lower_rate + upper_rate) / 2
        calculated_bond_price = calculate_bond_price(par_value, coupon_rate, ytm, years_to_maturity)

        if abs(calculated_bond_price - bond_price) < 0.01:
            return ytm
        elif calculated_bond_price < bond_price:
            upper_rate = ytm
        else:
            lower_rate = ytm

    return None

def calculate_years_to_maturity(par_value, coupon_rate, market_rate, bond_price):
    # Define the range of possible years for maturity calculation
    years = 1
    while years < 100:
        calculated_bond_price = calculate_bond_price(par_value, coupon_rate, market_rate, years)

        if abs(calculated_bond_price - bond_price) < 0.01:
            return years

        years += 1

    return None

def main():
    print("Bond Price and YTM Calculator")
    print("-------------------------------")

    option = input("Choose an option (1: Bond Price, 2: YTM, 3: Years to Maturity): ")

    if option == "1":
        par_value = float(input("Enter the par value (face value) of the bond: "))
        coupon_rate = float(input("Enter the annual coupon rate (as a decimal): "))
        market_rate = float(input("Enter the market interest rate (as a decimal): "))
        years_to_maturity = int(input("Enter the number of years to maturity: "))

        bond_price = calculate_bond_price(par_value, coupon_rate, market_rate, years_to_maturity)
        print(f"The price of the bond is: ${bond_price:.2f}")

    elif option == "2":
        par_value = float(input("Enter the par value (face value) of the bond: "))
        coupon_rate = float(input("Enter the annual coupon rate (as a decimal): "))
        bond_price = float(input("Enter the current bond price: "))
        years_to_maturity = int(input("Enter the number of years to maturity: "))

        ytm = calculate_yield_to_maturity(par_value, coupon_rate, bond_price, years_to_maturity)
        if ytm is not None:
            print(f"The Yield to Maturity (YTM) is: {ytm * 100:.2f}%")
        else:
            print("YTM calculation failed. Please check the input values.")

    elif option == "3":
        par_value = float(input("Enter the par value (face value) of the bond: "))
        coupon_rate = float(input("Enter the annual coupon rate (as a decimal): "))
        market_rate = float(input("Enter the market interest rate (as a decimal): "))
        bond_price = float(input("Enter the current bond price: "))

        years = calculate_years_to_maturity(par_value, coupon_rate, market_rate, bond_price)
        if years is not None:
            print(f"The number of years to maturity is: {years}")
        else:
            print("Years to maturity calculation failed. Please check the input values.")

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
