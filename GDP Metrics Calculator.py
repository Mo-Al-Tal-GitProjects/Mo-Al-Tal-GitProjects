def calculate_total_gdp(gdp_data):
    return sum(gdp_data.values())

def calculate_gdp_growth_rate(total_gdp, total_gdp_prev):
    return ((total_gdp - total_gdp_prev) / total_gdp_prev) * 100

def calculate_gdp_per_capita(total_gdp, population):
    return total_gdp / population

def get_gdp_data():
    gdp_data = {}
    sectors = ["Agriculture", "Manufacturing", "Services"]
    for sector in sectors:
        gdp = float(input(f"Enter GDP for {sector} (in billions of currency): "))
        gdp_data[sector] = gdp
    return gdp_data

def get_population():
    return float(input("Enter the population (in millions): "))

def get_gdp_data_prev():
    gdp_data_prev = {}
    sectors = ["Agriculture", "Manufacturing", "Services"]
    for sector in sectors:
        gdp_prev = float(input(f"Enter GDP for {sector} in the previous year (in billions of currency): "))
        gdp_data_prev[sector] = gdp_prev
    return gdp_data_prev

def main():
    print("GDP Metrics Calculator")
    gdp_data = get_gdp_data()
    total_gdp = calculate_total_gdp(gdp_data)

    population = get_population()

    gdp_data_prev = get_gdp_data_prev()
    total_gdp_prev = calculate_total_gdp(gdp_data_prev)

    gdp_growth_rate = calculate_gdp_growth_rate(total_gdp, total_gdp_prev)
    gdp_per_capita = calculate_gdp_per_capita(total_gdp, population)

    print(f"Total GDP: {total_gdp} billion")
    print(f"GDP Growth Rate: {gdp_growth_rate:.2f}%")
    print(f"GDP per Capita: {gdp_per_capita} billion")

if __name__ == "__main__":
    main()
