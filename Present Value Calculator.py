def calculate_present_value(N, I_Y, FV, PMT=0):
    try:
        # Calculate PV using the rearranged formula
        if I_Y == 0:
            PV = FV - PMT * N
        else:
            PV = FV / ((1 + I_Y)**N) - (PMT / I_Y) * ((1 + I_Y)**N - 1)
        return PV
    except ZeroDivisionError:
        print("Error: Annual interest rate (I/Y) cannot be zero.")

if __name__ == "__main__":
    print("Present Value Calculator")
    print("-----------------------")

    while True:
        try:
            # Get user input
            N = int(input("Enter the number of compounding periods (N): "))
            I_Y = float(input("Enter the annual interest rate (I/Y as a decimal): "))
            FV = float(input("Enter the future value (FV): "))
            PMT = float(input("Enter additional periodic payment (PMT, optional, enter 0 if none): "))

            # Calculate and display the present value
            PV = calculate_present_value(N, I_Y, FV, PMT)
            print(f"The present value (PV) is: {PV:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
