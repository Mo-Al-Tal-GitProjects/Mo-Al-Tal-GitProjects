def calculate_bond_yield(price, face_value, coupon_rate, years_to_maturity, frequency=1, guess=0.05, max_iterations=1000, tolerance=1e-6):
    # Convert annual coupon rate to periodic rate
    periodic_coupon_rate = coupon_rate / frequency

    # Calculate the number of periods
    periods = years_to_maturity * frequency

    # Define the objective function to find the yield
    def objective_function(yield_rate):
        present_value = 0
        for t in range(1, periods + 1):
            present_value += (periodic_coupon_rate * face_value) / (1 + yield_rate / frequency) ** (t)
        present_value += face_value / (1 + yield_rate / frequency) ** (periods)
        return price - present_value

    # Use the Newton-Raphson method to find the yield
    yield_estimate = guess
    for i in range(max_iterations):
        f_value = objective_function(yield_estimate)
        f_prime_value = objective_function(yield_estimate + 0.0001) - f_value
        yield_estimate = yield_estimate - f_value / f_prime_value
        if abs(f_value) < tolerance:
            return yield_estimate

    # If the method does not converge, return None
    return None

def main():
    print("Bond Yield Calculator")
    print("----------------------")

    price = float(input("Enter the bond's price: $"))
    face_value = float(input("Enter the face value of the bond: $"))
    coupon_rate = float(input("Enter the annual coupon rate (as a decimal): "))
    years_to_maturity = float(input("Enter the number of years to maturity: "))
    frequency = int(input("Enter the coupon payment frequency per year (e.g., 1 for annual, 2 for semi-annual): "))

    yield_rate = calculate_bond_yield(price, face_value, coupon_rate, years_to_maturity, frequency)

    if yield_rate is not None:
        print(f"The bond's yield to maturity is approximately: {yield_rate * 100:.2f}%")
    else:
        print("Failed to converge. Please check your inputs.")

if __name__ == "__main__":
    main()
