def calculate_gdp(C, G, I, NX):
    return C + G + I + NX

def main():
    user_lists = {}
    user_list_name = ""
    results = {}

    while True:
        print("GDP Calculator")
        print("Choose the variable to find:")
        print("1. GDP")
        print("2. Consumption (C)")
        print("3. Gov. Expenditures (G)")
        print("4. Investment (I)")
        print("5. Net Exports (NX)")
        print("6. Print lists")
        print("7. Quit")

        choice = input("Enter the option (1/2/3/4/5/6/7): ")

        C, G, I, NX, GDP = 0, 0, 0, 0, 0

        if choice == "1":
            C = float(input("Enter C: "))
            G = float(input("Enter G: "))
            I = float(input("Enter I: "))
            NX = float(input("Enter NX: "))
            GDP = calculate_gdp(C, G, I, NX)

        elif choice == "2":
            C = float(input("Enter C: "))
            G = float(input("Enter G: "))
            I = float(input("Enter I: "))
            NX = float(input("Enter NX: "))
            GDP = calculate_gdp(C, G, I, NX)

        elif choice == "3":
            C = float(input("Enter C: "))
            G = float(input("Enter G: "))
            I = float(input("Enter I: "))
            NX = float(input("Enter NX: "))
            GDP = calculate_gdp(C, G, I, NX)

        elif choice == "4":
            C = float(input("Enter C: "))
            G = float(input("Enter G: "))
            I = float(input("Enter I: "))
            NX = float(input("Enter NX: "))
            GDP = calculate_gdp(C, G, I, NX)

        elif choice == "5":
            C = float(input("Enter C: "))
            G = float(input("Enter G: "))
            I = float(input("Enter I: "))
            NX = float(input("Enter NX: "))
            GDP = calculate_gdp(C, G, I, NX)

        elif choice == "6":
            if user_lists:
                print("Lists created:")
                for list_name, data in user_lists.items():
                    print(f"List '{list_name}': {data}")
            else:
                print("No lists found.")
            continue  # Skip the prompt for user_list_name

        elif choice == "7":
            print("Exiting the GDP Calculator.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5/6/7).")

        results = {"GDP": GDP, "Consumption (C)": C, "Gov. Expenditures (G)": G, "Investment (I)": I, "Net Exports (NX)": NX}

        if choice not in ["6", "7"]:
            user_list_name = input("Enter a name for your list: ")
            if user_list_name:
                print(f"List '{user_list_name}' created.")
                user_lists[user_list_name] = results

if __name__ == "__main__":
    main()
