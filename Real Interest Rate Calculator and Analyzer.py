def calculate_real_interest_rate_difference(nominal_rate, inflation_rate):
    return nominal_rate - inflation_rate

def calculate_real_interest_rate_fischer(nominal_rate, inflation_rate):
    return ((1 + nominal_rate) / (1 + inflation_rate)) - 1

def calculate_average_real_interest_rate(real_interest_data):
    if not real_interest_data:
        return 0
    return sum(real_interest_data) / len(real_interest_data)

def main():
    real_interest_data = []

    while True:
        print("Real Interest Rate Calculator and Analyzer")
        print("Choose an option:")
        print("1. Calculate Real Interest Rate (Difference Method)")
        print("2. Calculate Real Interest Rate (Fischer's Equation)")
        print("3. Compare Real Interest Rate Data")
        print("4. Calculate Average Real Interest Rate")
        print("5. Forecast Future Real Interest Rate")
        print("6. Quit")

        choice = input("Enter the option (1/2/3/4/5/6): ")

        if choice == "1":
            nominal_rate = float(input("Enter the nominal interest rate: "))
            inflation_rate = float(input("Enter the inflation rate: "))
            real_interest_rate = calculate_real_interest_rate_difference(nominal_rate, inflation_rate)
            print(f"Real Interest Rate (Difference Method): {real_interest_rate:.2f}%")
            real_interest_data.append(real_interest_rate)

        elif choice == "2":
            nominal_rate = float(input("Enter the nominal interest rate: "))
            inflation_rate = float(input("Enter the inflation rate: "))
            real_interest_rate = calculate_real_interest_rate_fischer(nominal_rate, inflation_rate)
            print(f"Real Interest Rate (Fischer's Equation): {real_interest_rate:.2f}%")
            real_interest_data.append(real_interest_rate)

        elif choice == "3":
            if not real_interest_data:
                print("No data available for comparison.")
            else:
                print("Real Interest Rate Data Comparison:")
                for idx, rate in enumerate(real_interest_data, start=1):
                    print(f"Year {idx}: Real Interest Rate - {rate:.2f}%")

        elif choice == "4":
            avg_real_interest_rate = calculate_average_real_interest_rate(real_interest_data)
            print(f"Average Real Interest Rate: {avg_real_interest_rate:.2f}%")

        elif choice == "5":
            if not real_interest_data:
                print("No data available for forecasting.")
            else:
                forecast_year = int(input("Enter the year for real interest rate forecasting: "))
                avg_real_interest_rate = calculate_average_real_interest_rate(real_interest_data)
                forecasted_real_interest_rate = avg_real_interest_rate
                print(f"Forecasted Real Interest Rate for Year {forecast_year}: {forecasted_real_interest_rate:.2f}%")

        elif choice == "6":
            print("Exiting the Real Interest Rate Calculator and Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5/6).")

if __name__ == "__main__":
    main()
