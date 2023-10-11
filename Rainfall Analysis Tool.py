def collect_rainfall_data():
    years = int(input("Enter the Number of Years: "))
    rainfall_data = []

    for year in range(1, years + 1):
        monthly_rainfall = []
        for month in range(1, 13):
            monthly_rain = float(input(f"Enter Month {month} rainfall (in inches) for Year {year}: "))
            monthly_rainfall.append(monthly_rain)
        rainfall_data.append(monthly_rainfall)

    return rainfall_data

def calculate_statistics(data):
    total_rainfall = sum(sum(monthly) for monthly in data)
    avg_monthly_rainfall = total_rainfall / (len(data) * 12)
    
    wettest_year = max(data, key=lambda yearly_rainfall: sum(yearly_rainfall))
    driest_year = min(data, key=lambda yearly_rainfall: sum(yearly_rainfall))
    
    wettest_month = data[0].index(max(data[0]))
    driest_month = data[0].index(min(data[0]))
    
    return total_rainfall, avg_monthly_rainfall, wettest_year, driest_year, wettest_month, driest_month

def display_results(total_rainfall, avg_monthly_rainfall, wettest_year, driest_year, wettest_month, driest_month):
    print(f"Total Rainfall: {total_rainfall} inches")
    print(f"Average Monthly Rainfall: {avg_monthly_rainfall:.2f} inches")
    print(f"Wettest Year: Year {wettest_year + 1}")
    print(f"Driest Year: Year {driest_year + 1}")
    print(f"Wettest Month: Month {wettest_month + 1}")
    print(f"Driest Month: Month {driest_month + 1}")

def plot_monthly_rainfall(data):
    import matplotlib.pyplot as plt

    # Extract data for the first year for plotting
    monthly_rainfall = data[0]

    months = range(1, 13)
    plt.bar(months, monthly_rainfall, tick_label=months)
    plt.xlabel("Month")
    plt.ylabel("Rainfall (inches)")
    plt.title("Monthly Rainfall for the First Year")
    plt.show()

def main():
    print("Rainfall Analysis Tool")
    print("-----------------------")

    data = collect_rainfall_data()
    total_rainfall, avg_monthly_rainfall, wettest_year, driest_year, wettest_month, driest_month = calculate_statistics(data)
    display_results(total_rainfall, avg_monthly_rainfall, wettest_year, driest_year, wettest_month, driest_month)
    
    # Additional feature: Plot monthly rainfall for the first year
    plot_monthly_rainfall(data)

if __name__ == "__main__":
    main()
