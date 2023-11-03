class EconomicIndicatorCalculator:
    def calculate_total_revenue(self, price, quantity):
        return price * quantity

    def calculate_marginal_revenue(self, change_in_total_revenues, change_in_quantity_traded):
        return change_in_total_revenues / change_in_quantity_traded

    def calculate_average_revenue(self, total_income, total_quantity):
        return total_income / total_quantity

    def calculate_total_costs(self, fixed_costs, variable_costs):
        return fixed_costs + variable_costs

    def calculate_marginal_costs(self, change_in_total_costs, change_in_quantity_produced):
        return change_in_total_costs / change_in_quantity_produced

    def calculate_average_cost(self, total_costs, total_quantity):
        return total_costs / total_quantity

    def calculate_average_fixed_cost(self, total_fixed_costs, total_quantity):
        return total_fixed_costs / total_quantity

    def calculate_average_variable_cost(self, total_variable_costs, total_quantity):
        return total_variable_costs / total_quantity

    def calculate_profit(self, total_revenue, total_costs):
        return total_revenue - total_costs

    def run_calculator(self):
        print("Economic Indicator Calculator")
        print("Choose the indicator to calculate:")
        print("1. Total Revenue")
        print("2. Marginal Revenue")
        print("3. Average Revenue")
        print("4. Total Costs")
        print("5. Marginal Costs")
        print("6. Average Cost")
        print("7. Average Fixed Cost")
        print("8. Average Variable Cost")
        print("9. Profit Earned")
        choice = int(input("Enter the option (1-9): "))

        if choice < 1 or choice > 9:
            print("Invalid option. Please choose a valid option (1-9).")
            return

        if choice in [1, 2, 3]:
            input1 = float(input("Enter the first value: "))
            input2 = float(input("Enter the second value: "))
        elif choice in [4, 5, 6, 7, 8, 9]:
            input1 = float(input("Enter the first value: "))
            input2 = float(input("Enter the second value: "))

        if choice == 1:
            result = self.calculate_total_revenue(input1, input2)
            print(f"Total Revenue: {result}")
        elif choice == 2:
            result = self.calculate_marginal_revenue(input1, input2)
            print(f"Marginal Revenue: {result}")
        elif choice == 3:
            result = self.calculate_average_revenue(input1, input2)
            print(f"Average Revenue: {result}")
        elif choice == 4:
            result = self.calculate_total_costs(input1, input2)
            print(f"Total Costs: {result}")
        elif choice == 5:
            result = self.calculate_marginal_costs(input1, input2)
            print(f"Marginal Costs: {result}")
        elif choice == 6:
            result = self.calculate_average_cost(input1, input2)
            print(f"Average Cost: {result}")
        elif choice == 7:
            result = self.calculate_average_fixed_cost(input1, input2)
            print(f"Average Fixed Cost: {result}")
        elif choice == 8:
            result = self.calculate_average_variable_cost(input1, input2)
            print(f"Average Variable Cost: {result}")
        elif choice == 9:
            result = self.calculate_profit(input1, input2)
            print(f"Profit Earned: {result}")
if __name__ == "__main__":
    calculator = EconomicIndicatorCalculator()
    calculator.run_calculator()
