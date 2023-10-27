def calculate_money_multiplier(reserve_ratio):
    if reserve_ratio != 0:
        return 1 / reserve_ratio
    else:
        return 0

def main():
    money_multiplier_data = []

    while True:
        print("Money Multiplier Rate Calculator")
        print("Choose an option:")
        print("1. Calculate Money Multiplier Rate")
        print("2. View Money Multiplier Data")
        print("3. Quit")

        choice = input("Enter the option (1/2/3): ")

        if choice == "1":
            reserve_ratio = float(input("Enter the reserve ratio: "))
            money_multiplier = calculate_money_multiplier(reserve_ratio)
            print(f"Money Multiplier Rate: {money_multiplier}")
            money_multiplier_data.append(money_multiplier)

        elif choice == "2":
            if not money_multiplier_data:
                print("No data available.")
            else:
                print("Money Multiplier Data:")
                for idx, rate in enumerate(money_multiplier_data, start=1):
                    print(f"Entry {idx}: {rate:.2f}")

        elif choice == "3":
            print("Exiting the Money Multiplier Rate Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3).")

if __name__ == "__main__":
    main()
