def calculate_future_value(N, I_Y, PV, PMT=0):
    # Calculate FV using the formula
    FV = PV * (1 + I_Y)**N + PMT * ((1 + I_Y)**N - 1) / I_Y
    return FV

if __name__ == "__main__":
    print("Compounding Value Calculator")
    print("-----------------------------")

    while True:
        try:
            # Get user input
            N = int(input("Enter the number of compounding periods (N): "))
            I_Y = float(input("Enter the annual interest rate (I/Y as a decimal): "))
            PV = float(input("Enter the present value (PV): "))
            PMT = float(input("Enter additional periodic payment (PMT, optional, enter 0 if none): "))

            # Calculate and display the future value
            FV = calculate_future_value(N, I_Y, PV, PMT)
            print(f"The future value (FV) is: {FV:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
