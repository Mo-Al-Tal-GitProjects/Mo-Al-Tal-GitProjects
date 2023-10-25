def calculate_gdp(W, I, R, P):
    return W + I + R + P

def main():
    user_lists = {}
    user_list_name = ""
    results = {}

    while True:
        print("GDP Calculator (Income Approach)")
        print("Choose the variable to find:")
        print("1. GDP")
        print("2. Labor Income (W)")
        print("3. Interest Income (I)")
        print("4. Rent Income (R)")
        print("5. Profit Income (P)")
        print("6. Print lists")
        print("7. Quit")

        choice = input("Enter the option (1/2/3/4/5/6/7): ")

        W, I, R, P, GDP = 0, 0, 0, 0, 0

        if choice == "1":
            W = float(input("Enter Labor Income (W): "))
            I = float(input("Enter Interest Income (I): "))
            R = float(input("Enter Rent Income (R): "))
            P = float(input("Enter Profit Income (P): "))
            GDP = calculate_gdp(W, I, R, P)

        elif choice == "2":
            W = float(input("Enter Labor Income (W): "))
            I = float(input("Enter Interest Income (I): "))
            R = float(input("Enter Rent Income (R): "))
            P = float(input("Enter Profit Income (P): "))
            GDP = calculate_gdp(W, I, R, P)

        elif choice == "3":
            W = float(input("Enter Labor Income (W): "))
            I = float(input("Enter Interest Income (I): "))
            R = float(input("Enter Rent Income (R): "))
            P = float(input("Enter Profit Income (P): "))
            GDP = calculate_gdp(W, I, R, P)

        elif choice == "4":
            W = float(input("Enter Labor Income (W): "))
            I = float(input("Enter Interest Income (I): "))
            R = float(input("Enter Rent Income (R): "))
            P = float(input("Enter Profit Income (P): "))
            GDP = calculate_gdp(W, I, R, P)

        elif choice == "5":
            W = float(input("Enter Labor Income (W): "))
            I = float(input("Enter Interest Income (I): "))
            R = float(input("Enter Rent Income (R): "))
            P = float(input("Enter Profit Income (P): "))
            GDP = calculate_gdp(W, I, R, P)

        elif choice == "6":
            if user_lists:
                print("Lists created:")
                for list_name, data in user_lists.items():
                    print(f"List '{list_name}': {data}")
            else:
                print("No lists found.")
            continue  # Skip the prompt for user_list_name

        elif choice == "7":
            print("Exiting the GDP Calculator (Income Approach).")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5/6/7).")

        results = {"GDP": GDP, "Labor Income (W)": W, "Interest Income (I)": I, "Rent Income (R)": R, "Profit Income (P)": P}

        if choice not in ["6", "7"]:
            user_list_name = input("Enter a name for your list: ")
            if user_list_name:
                print(f"List '{user_list_name}' created.")
                user_lists[user_list_name] = results

if __name__ == "__main__":
    main()
