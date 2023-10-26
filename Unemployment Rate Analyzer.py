import statistics

def calculate_unemployment_rate(unemployed, employed):
    if employed > 0:
        return (unemployed / employed) * 100
    else:
        return 0

def main():
    unemployment_data = []

    while True:
        print("Unemployment Rate Calculator and Analysis")
        print("Choose an option:")
        print("1. Calculate Unemployment Rate")
        print("2. Analyze Unemployment Data")
        print("3. Print Historical Data")
        print("4. Quit")

        choice = input("Enter the option (1/2/3/4): ")

        if choice == "1":
            unemployed = int(input("Enter the total number of unemployed individuals: "))
            employed = int(input("Enter the total number of employed individuals: "))
            rate = calculate_unemployment_rate(unemployed, employed)
            date = input("Enter the date (e.g., YYYY-MM-DD): ")
            unemployment_data.append({"Date": date, "Unemployed": unemployed, "Employed": employed, "Unemployment Rate": rate})
            print(f"Unemployment Rate: {rate:.2f}%")

        elif choice == "2":
            if not unemployment_data:
                print("No data available.")
            else:
                print("Unemployment Data Analysis:")
                unemployment_rates = [data["Unemployment Rate"] for data in unemployment_data]
                average_rate = statistics.mean(unemployment_rates)
                max_rate = max(unemployment_rates)
                min_rate = min(unemployment_rates)
                print(f"Average Unemployment Rate: {average_rate:.2f}%")
                print(f"Maximum Unemployment Rate: {max_rate:.2f}%")
                print(f"Minimum Unemployment Rate: {min_rate:.2f}%")

        elif choice == "3":
            if not unemployment_data:
                print("No historical data available.")
            else:
                print("Historical Unemployment Data:")
                for data in unemployment_data:
                    print(f"Date: {data['Date']}, Unemployed: {data['Unemployed']}, Employed: {data['Employed']}, Unemployment Rate: {data['Unemployment Rate']:.2f}%")

        elif choice == "4":
            print("Exiting the Unemployment Rate Calculator and Analysis.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
