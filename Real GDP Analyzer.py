def calculate_real_gdp(nominal_gdp, gdp_deflator):
    return nominal_gdp / gdp_deflator

def main():
    real_gdp_data = []

    while True:
        print("Real GDP Calculator and Analyzer")
        print("Choose an option:")
        print("1. Calculate Real GDP")
        print("2. Compare Real GDP Data")
        print("3. Quit")

        choice = input("Enter the option (1/2/3): ")

        if choice == "1":
            nominal_gdp = float(input("Enter Nominal GDP: "))
            gdp_deflator = float(input("Enter GDP Deflator: "))
            real_gdp = calculate_real_gdp(nominal_gdp, gdp_deflator)
            print(f"Real GDP: {real_gdp:.2f}")
            real_gdp_data.append(real_gdp)

        elif choice == "2":
            if not real_gdp_data:
                print("No data available for comparison.")
            else:
                print("Real GDP Data Comparison:")
                for idx, gdp in enumerate(real_gdp_data, start=1):
                    print(f"Year {idx}: Real GDP - {gdp:.2f}")

                growth_rate = (real_gdp_data[-1] - real_gdp_data[0]) / real_gdp_data[0]
                print(f"Growth Rate: {growth_rate:.2%}")

        elif choice == "3":
            print("Exiting the Real GDP Calculator and Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

if __name__ == "__main__":
    main()
