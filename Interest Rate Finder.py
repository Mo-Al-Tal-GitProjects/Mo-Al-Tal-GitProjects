def calculate_interest_rate(N, PV, FV, PMT=0):
    try:
        # Calculate I/Y using the rearranged formula
        if PV == 0:
            I_Y = (FV - PMT * N) / (PMT * N)
        else:
            I_Y = ((FV / PV) ** (1 / N)) - 1
        return I_Y * 100  # Convert to percentage
    except ZeroDivisionError:
        print("Error: Number of compounding periods (N) cannot be zero.")

if __name__ == "__main__":
    print("Interest Rate Calculator")
    print("-----------------------")

    while True:
        try:
            # Get user input
            N = int(input("Enter the number of compounding periods (N): "))
            PV = float(input("Enter the present value (PV): "))
            FV = float(input("Enter the future value (FV): "))
            PMT = float(input("Enter additional periodic payment (PMT, optional, enter 0 if none): "))

            # Calculate and display the interest rate
            I_Y = calculate_interest_rate(N, PV, FV, PMT)
            print(f"The annual interest rate (I/Y) is: {I_Y:.2f}%")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
