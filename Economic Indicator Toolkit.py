class EconomicIndicatorToolkit:
    def __init__(self):
        self.data = {}

    def calculate_nominal_gdp(self, consumption, government_expenditure, investment, net_exports):
        return consumption + government_expenditure + investment + net_exports

    def calculate_real_gdp(self, nominal_gdp, gdp_deflator):
        return nominal_gdp / gdp_deflator

    def calculate_consumer_price_index(self, cost_given_year, cost_base_year):
        return cost_given_year / cost_base_year

    def calculate_inflation_rate(self, cpi_current_year, cpi_last_year):
        return ((cpi_current_year - cpi_last_year) / cpi_last_year) * 100

    def calculate_real_interest_rate(self, nominal_rate, inflation_rate):
        return (1 + nominal_rate) / (1 + inflation_rate) - 1

    def calculate_quantity_theory_of_money(self, m, v, p, t):
        return m * v - p * t

    def calculate_total_revenue(self, price, quantity):
        return price * quantity

    def calculate_marginal_revenue(self, delta_total_revenue, delta_quantity):
        return delta_total_revenue / delta_quantity

    def calculate_average_revenue(self, total_income, total_quantity):
        return total_income / total_quantity

    def calculate_total_cost(self, fixed_costs, variable_costs):
        return fixed_costs + variable_costs

    def calculate_marginal_cost(self, delta_total_costs, delta_quantity):
        return delta_total_costs / delta_quantity

    def calculate_average_total_cost(self, total_costs, total_quantity):
        return total_costs / total_quantity

    def calculate_average_fixed_costs(self, total_fixed_costs, total_quantity):
        return total_fixed_costs / total_quantity

    def calculate_average_variable_costs(self, total_variable_costs, total_quantity):
        return total_variable_costs / total_quantity

    def calculate_profit(self, total_revenue, total_costs):
        return total_revenue - total_costs

    def run(self):
        while True:
            print("Economic Indicator Toolkit")
            print("Choose an option:")
            print("1. Calculate Macroeconomic Indicator")
            print("2. Calculate Microeconomic Indicator")
            print("3. Quit")
            choice = input("Enter the option (1/2/3): ")

            if choice == "1":
                self.calculate_macroeconomic_indicator()
            elif choice == "2":
                self.calculate_microeconomic_indicator()
            elif choice == "3":
                print("Exiting the Economic Indicator Toolkit.")
                break
            else:
                print("Invalid option. Please choose a valid option (1/2/3).")

    def calculate_macroeconomic_indicator(self):
        print("Choose a macroeconomic indicator to calculate:")
        print("1. Nominal GDP")
        print("2. Real GDP")
        print("3. Consumer Price Index")
        print("4. Inflation Rate")
        print("5. Real Interest Rate")
        print("6. Quantity Theory of Money")
        indicator_choice = input("Enter the indicator choice (1/2/3/4/5/6): ")

        if indicator_choice == "1":
            consumption = float(input("Enter Consumption (C): "))
            government_expenditure = float(input("Enter Gov. Expenditure (G): "))
            investment = float(input("Enter Investment (I): "))
            net_exports = float(input("Enter Net Exports (NX): "))
            nominal_gdp = self.calculate_nominal_gdp(consumption, government_expenditure, investment, net_exports)
            self.data["Nominal GDP"] = nominal_gdp
            print(f"Nominal GDP: {nominal_gdp}")
        elif indicator_choice == "2":
            nominal_gdp = float(input("Enter Nominal GDP: "))
            gdp_deflator = float(input("Enter GDP Deflator: "))
            real_gdp = self.calculate_real_gdp(nominal_gdp, gdp_deflator)
            self.data["Real GDP"] = real_gdp
            print(f"Real GDP: {real_gdp}")
        elif indicator_choice == "3":
            cost_given_year = float(input("Enter Cost for Given Year: "))
            cost_base_year = float(input("Enter Cost for Base Year: "))
            cpi = self.calculate_consumer_price_index(cost_given_year, cost_base_year)
            self.data["Consumer Price Index"] = cpi
            print(f"Consumer Price Index: {cpi}")
        elif indicator_choice == "4":
            cpi_current_year = float(input("Enter CPI for Current Year: "))
            cpi_last_year = float(input("Enter CPI for Last Year: "))
            inflation_rate = self.calculate_inflation_rate(cpi_current_year, cpi_last_year)
            self.data["Inflation Rate"] = inflation_rate
            print(f"Inflation Rate: {inflation_rate}")
        elif indicator_choice == "5":
            nominal_rate = float(input("Enter Nominal Interest Rate: "))
            inflation_rate = float(input("Enter Inflation Rate: "))
            real_interest_rate = self.calculate_real_interest_rate(nominal_rate, inflation_rate)
            self.data["Real Interest Rate"] = real_interest_rate
            print(f"Real Interest Rate: {real_interest_rate}")
        elif indicator_choice == "6":
            m = float(input("Enter Money Supply (M): "))
            v = float(input("Enter Velocity of Money (V): "))
            p = float(input("Enter Price Level (P): "))
            t = float(input("Enter Transaction Volume (T): "))
            quantity_theory_result = self.calculate_quantity_theory_of_money(m, v, p, t)
            self.data["Quantity Theory of Money"] = quantity_theory_result
            print(f"Quantity Theory of Money: {quantity_theory_result}")
        else:
            print("Invalid indicator choice. Please choose a valid option (1/2/3/4/5/6).")

    def calculate_microeconomic_indicator(self):
        print("Choose a microeconomic indicator to calculate:")
        print("1. Total Revenue")
        print("2. Marginal Revenue")
        print("3. Average Revenue")
        print("4. Total Cost")
        print("5. Marginal Cost")
        print("6. Average Total Cost")
        print("7. Average Fixed Costs")
        print("8. Average Variable Costs")
        print("9. Profit Margin")
        indicator_choice = input("Enter the indicator choice (1/2/3/4/5/6/7/8/9): ")

        if indicator_choice == "1":
            price = float(input("Enter Price: "))
            quantity = float(input("Enter Quantity: "))
            total_revenue = self.calculate_total_revenue(price, quantity)
            self.data["Total Revenue"] = total_revenue
            print(f"Total Revenue: {total_revenue}")
        elif indicator_choice == "2":
            delta_total_revenue = float(input("Enter Delta Total Revenue: "))
            delta_quantity = float(input("Enter Delta Quantity: "))
            marginal_revenue = self.calculate_marginal_revenue(delta_total_revenue, delta_quantity)
            self.data["Marginal Revenue"] = marginal_revenue
            print(f"Marginal Revenue: {marginal_revenue}")
        elif indicator_choice == "3":
            total_income = float(input("Enter Total Income: "))
            total_quantity = float(input("Enter Total Quantity: "))
            average_revenue = self.calculate_average_revenue(total_income, total_quantity)
            self.data["Average Revenue"] = average_revenue
            print(f"Average Revenue: {average_revenue}")
        elif indicator_choice == "4":
            fixed_costs = float(input("Enter Fixed Costs: "))
            variable_costs = float(input("Enter Variable Costs: "))
            total_costs = self.calculate_total_cost(fixed_costs, variable_costs)
            self.data["Total Cost"] = total_costs
            print(f"Total Cost: {total_costs}")
        elif indicator_choice == "5":
            delta_total_costs = float(input("Enter Delta Total Costs: "))
            delta_quantity = float(input("Enter Delta Quantity: "))
            marginal_cost = self.calculate_marginal_cost(delta_total_costs, delta_quantity)
            self.data["Marginal Cost"] = marginal_cost
            print(f"Marginal Cost: {marginal_cost}")
        elif indicator_choice == "6":
            total_costs = float(input("Enter Total Costs: "))
            total_quantity = float(input("Enter Total Quantity: "))
            average_total_cost = self.calculate_average_total_cost(total_costs, total_quantity)
            self.data["Average Total Cost"] = average_total_cost
            print(f"Average Total Cost: {average_total_cost}")
        elif indicator_choice == "7":
            total_fixed_costs = float(input("Enter Total Fixed Costs: "))
            total_quantity = float(input("Enter Total Quantity: "))
            average_fixed_costs = self.calculate_average_fixed_costs(total_fixed_costs, total_quantity)
            self.data["Average Fixed Costs"] = average_fixed_costs
            print(f"Average Fixed Costs: {average_fixed_costs}")
        elif indicator_choice == "8":
            total_variable_costs = float(input("Enter Total Variable Costs: "))
            total_quantity = float(input("Enter Total Quantity: "))
            average_variable_costs = self.calculate_average_variable_costs(total_variable_costs, total_quantity)
            self.data["Average Variable Costs"] = average_variable_costs
            print(f"Average Variable Costs: {average_variable_costs}")
        elif indicator_choice == "9":
            total_revenue = float(input("Enter Total Revenue: "))
            total_costs = float(input("Enter Total Costs: "))
            profit_margin = self.calculate_profit(total_revenue, total_costs)
            self.data["Profit Margin"] = profit_margin
            print(f"Profit Margin: {profit_margin}")
        else:
            print("Invalid indicator choice. Please choose a valid option (1/2/3/4/5/6/7/8/9).")

if __name__ == "__main__":
    economic_toolkit = EconomicIndicatorToolkit()
    economic_toolkit.run()
