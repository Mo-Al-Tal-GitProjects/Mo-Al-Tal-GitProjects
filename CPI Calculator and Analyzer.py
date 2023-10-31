def calculate_cpi(cost_year, cost_base):
    return (cost_year / cost_base) * 100

def main():
    cpi_data = []
    base_year = None

    while True:
        print("Consumer Price Index (CPI) Calculator and Analyzer")
        print("Choose an option:")
        print("1. Calculate CPI")
        print("2. Update Base Year")
        print("3. Compare CPI Data")
        print("4. Forecast Future CPI")
        print("5. Quit")

        choice = input("Enter the option (1/2/3/4/5): ")

        if choice == "1":
            if base_year is None:
                print("Please set the base year first.")
            else:
                cost_year = float(input("Enter the cost of products and services for the given year: "))
                cpi = calculate_cpi(cost_year, cost_base)
                print(f"CPI for Year {base_year}: {cpi:.2f}")
                cpi_data.append((base_year, cpi))

        elif choice == "2":
            base_year = int(input("Enter the new base year: "))
            cost_base = float(input("Enter the cost of products and services for the new base year: "))
            print(f"Base year updated to {base_year} with CPI of {cost_base:.2f}")

        elif choice == "3":
            if not cpi_data:
                print("No data available for comparison.")
            else:
                print("CPI Data Comparison:")
                for year, cpi in cpi_data:
                    print(f"Year {year}: CPI - {cpi:.2f}")

                inflation_rate = (cpi_data[-1][1] - cpi_data[0][1]) / cpi_data[0][1]
                print(f"Inflation Rate: {inflation_rate:.2%}")

        elif choice == "4":
            if base_year is None:
                print("Please set the base year first.")
            else:
                forecast_year = int(input("Enter the year for CPI forecasting: "))
                forecasted_cpi = cpi_data[0][1] * (1 + inflation_rate) ** (forecast_year - cpi_data[0][0])
                print(f"Forecasted CPI for Year {forecast_year}: {forecasted_cpi:.2f}")

        elif choice == "5":
            print("Exiting the CPI Calculator and Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
