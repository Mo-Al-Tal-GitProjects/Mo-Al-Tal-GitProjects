import statistics

# Dictionary to store datasets
datasets = {}

# Function to calculate the mean
def calculate_mean(observations):
    return sum(observations) / len(observations)

# Function to calculate the median
def calculate_median(observations):
    return statistics.median(observations)

# Function to calculate the mode
def calculate_mode(observations):
    try:
        return statistics.mode(observations)
    except statistics.StatisticsError as e:
        return f"No unique mode found: {e}"

# Function to calculate the variance
def calculate_variance(observations):
    return statistics.variance(observations)

# Function to calculate the standard deviation
def calculate_std_deviation(observations):
    return statistics.stdev(observations)

# Main function
def main():
    print("Welcome to the Statistics Calculator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new dataset")
        print("2. Calculate statistics for a dataset")
        print("3. List existing datasets")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            dataset_name = input("Enter a name for your dataset: ")
            data = input("Enter your data separated by spaces (e.g., 1 2 3 4 5): ")
            observations = [float(x) for x in data.split()]
            datasets[dataset_name] = observations
        elif choice == '2':
            dataset_name = input("Enter the name of the dataset: ")
            if dataset_name in datasets:
                observations = datasets[dataset_name]
                print(f"Statistics for dataset '{dataset_name}':")
                print(f"Mean: {calculate_mean(observations)}")
                print(f"Median: {calculate_median(observations)}")
                print(f"Mode: {calculate_mode(observations)}")
                print(f"Variance: {calculate_variance(observations)}")
                print(f"Standard Deviation: {calculate_std_deviation(observations)}")
            else:
                print(f"Dataset '{dataset_name}' not found.")
        elif choice == '3':
            print("Existing datasets:")
            for name in datasets:
                print(name)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
