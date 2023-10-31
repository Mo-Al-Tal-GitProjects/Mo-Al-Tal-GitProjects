def calculate_inflation_rate(current_cpi, last_year_cpi):
    changes_in_cpi = current_cpi - last_year_cpi
    return (changes_in_cpi / last_year_cpi) * 100

def calculate_average_inflation_rate(inflation_data):
    if not inflation_data:
        return 0
    return sum(inflation_data) / len(inflation_data)

def main():
    inflation_data = []

    while True:
        print("Inflation Rate Calculator and Analyzer")
        print("Choose an option:")
        print("1. Calculate Inflation Rate")
        print("2. Compare Inflation Rate Data")
        print("3. Calculate Average Inflation Rate")
        print("4. Forecast Future Inflation Rate")
        print("5. Quit")

        choice = input("Enter the option (1/2/3/4/5): ")

        if choice == "1":
            current_cpi = float(input("Enter the CPI level for the current year: "))
            last_year_cpi = float(input("Enter the CPI level for the last year: "))
            inflation_rate = calculate_inflation_rate(current_cpi, last_year_cpi)
            print(f"Inflation Rate: {inflation_rate:.2f}%")
            inflation_data.append(inflation_rate)

        elif choice == "2":
            if not inflation_data:
                print("No data available for comparison.")
            else:
                print("Inflation Rate Data Comparison:")
                for idx, rate in enumerate(inflation_data, start=1):
                    print(f"Year {idx}: Inflation Rate - {rate:.2f}%")

        elif choice == "3":
            avg_inflation_rate = calculate_average_inflation_rate(inflation_data)
            print(f"Average Inflation Rate: {avg_inflation_rate:.2f}%")

        elif choice == "4":
            if not inflation_data:
                print("No data available for forecasting.")
            else:
                forecast_year = int(input("Enter the year for inflation rate forecasting: "))
                avg_inflation_rate = calculate_average_inflation_rate(inflation_data)
                forecasted_inflation_rate = avg_inflation_rate
                print(f"Forecasted Inflation Rate for Year {forecast_year}: {forecasted_inflation_rate:.2f}%")

        elif choice == "5":
            print("Exiting the Inflation Rate Calculator and Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
