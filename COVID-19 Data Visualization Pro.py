import matplotlib.pyplot as plt

# Function to input COVID-19 data manually
def input_covid_data():
    dates = []
    cases = []
    while True:
        date = input("Enter date (YYYY-MM-DD) or 'done' to finish: ")
        if date.lower() == 'done':
            break
        try:
            cases_count = int(input("Enter the number of confirmed cases: "))
            dates.append(date)
            cases.append(cases_count)
        except ValueError:
            print("Invalid input. Please enter a valid date and cases count.")
    return dates, cases

# Function to create a line chart for COVID-19 cases
def create_covid_chart(dates, cases):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, cases, marker='o', linestyle='-', color='b')
    plt.title("COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()

# Function to save the chart to a file
def save_chart_to_file(dates, cases, filename):
    create_covid_chart(dates, cases)
    plt.savefig(filename)
    print(f"Chart saved as '{filename}'.")

# Main function
def main():
    print("Welcome to the Advanced COVID-19 Data Visualizer!")
    
    dates, cases = input_covid_data()
    
    if len(dates) > 0:
        create_covid_chart(dates, cases)
        
        while True:
            action = input("Do you want to save the chart to a file? (yes/no): ").lower()
            if action == 'yes':
                filename = input("Enter the filename (e.g., chart.png): ")
                save_chart_to_file(dates, cases, filename)
                break
            elif action == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        plt.show()
    else:
        print("No COVID-19 data provided.")

if __name__ == "__main__":
    main()
