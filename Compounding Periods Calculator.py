def calculate_compounding_periods(I_Y, PV, FV, PMT=0):
    try:
        # Calculate N using the rearranged formula
        if I_Y == 0:
            N = (FV - PV) / (PMT if PMT != 0 else 1)
        else:
            N = (math.log(FV / (PV + PMT * I_Y)) / math.log(1 + I_Y))
        return N
    except ZeroDivisionError:
        print("Error: Annual interest rate (I/Y) cannot be zero.")

import math

if __name__ == "__main__":
    print("Compounding Periods Calculator")
    print("------------------------------")

    while True:
        try:
            # Get user input
            I_Y = float(input("Enter the annual interest rate (I/Y as a decimal): "))
            PV = float(input("Enter the present value (PV): "))
            FV = float(input("Enter the future value (FV): "))
            PMT = float(input("Enter additional periodic payment (PMT, optional, enter 0 if none): "))

            # Calculate and display the number of compounding periods
            N = calculate_compounding_periods(I_Y, PV, FV, PMT)
            print(f"The number of compounding periods (N) is: {N:.2f}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
