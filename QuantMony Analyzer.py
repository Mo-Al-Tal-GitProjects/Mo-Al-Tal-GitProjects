def calculate_quantity_theory(M, V, P, T):
    if M is None:
        return P * T / V
    elif V is None:
        return P * T / M
    elif P is None:
        return M * V / T
    elif T is None:
        return M * V / P

def main():
    quantity_theory_data = []

    while True:
        print("Quantity Theory of Money Calculator and Analyzer")
        print("Choose an option:")
        print("1. Calculate a Variable")
        print("2. Compare Historical Data")
        print("3. Project Future Data")
        print("4. Quit")

        choice = input("Enter the option (1/2/3/4): ")

        M, V, P, T = None, None, None, None

        if choice == "1":
            variable_to_calculate = input("Enter the variable to calculate (M/V/P/T): ").upper()

            if variable_to_calculate == "M":
                P = float(input("Enter Price Level (P): "))
                T = float(input("Enter Transaction Volume (T): "))
                V = float(input("Enter Velocity of Money (V): "))
                M = calculate_quantity_theory(M, V, P, T)
                print(f"Money Supply (M): {M}")
                # Store historical data
                quantity_theory_data.append({'M': M, 'V': V, 'P': P, 'T': T})

            elif variable_to_calculate == "V":
                M = float(input("Enter Money Supply (M): "))
                T = float(input("Enter Transaction Volume (T): "))
                P = float(input("Enter Price Level (P): "))
                V = calculate_quantity_theory(M, V, P, T)
                print(f"Velocity of Money (V): {V}")
                # Store historical data
                quantity_theory_data.append({'M': M, 'V': V, 'P': P, 'T': T})

            elif variable_to_calculate == "P":
                M = float(input("Enter Money Supply (M): "))
                V = float(input("Enter Velocity of Money (V): "))
                T = float(input("Enter Transaction Volume (T): "))
                P = calculate_quantity_theory(M, V, P, T)
                print(f"Price Level (P): {P}")
                # Store historical data
                quantity_theory_data.append({'M': M, 'V': V, 'P': P, 'T': T})

            elif variable_to_calculate == "T":
                M = float(input("Enter Money Supply (M): "))
                V = float(input("Enter Velocity of Money (V): "))
                P = float(input("Enter Price Level (P): "))
                T = calculate_quantity_theory(M, V, P, T)
                print(f"Transaction Volume (T): {T}")
                # Store historical data
                quantity_theory_data.append({'M': M, 'V': V, 'P': P, 'T': T})

            else:
                print("Invalid variable. Please enter M, V, P, or T.")

        elif choice == "2":
            if not quantity_theory_data:
                print("No historical data available for comparison.")
            else:
                print("Historical Quantity Theory Data Comparison:")
                for data_point in quantity_theory_data:
                    print(f"M: {data_point['M']}, V: {data_point['V']}, P: {data_point['P']}, T: {data_point['T']}")

        elif choice == "3":
            if not quantity_theory_data:
                print("No historical data available for forecasting.")
            else:
                forecast_year = int(input("Enter the year for data projection: "))
                projected_data = quantity_theory_data[-1].copy()
                projected_data["Year"] = forecast_year
                quantity_theory_data.append(projected_data)
                print(f"Projected Data for Year {forecast_year}: M: {projected_data['M']}, V: {projected_data['V']}, P: {projected_data['P']}, T: {projected_data['T']}")

        elif choice == "4":
            print("Exiting the Quantity Theory of Money Calculator and Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
