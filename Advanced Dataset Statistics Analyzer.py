import statistics
import math

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

# Function to calculate the coefficient of variation
def calculate_coeff_of_variation(observations):
    mean = calculate_mean(observations)
    std_deviation = calculate_std_deviation(observations)
    return (std_deviation / mean) * 100 if mean != 0 else 0

# Function to calculate the skewness of the data
def calculate_skewness(observations):
    mean = calculate_mean(observations)
    std_deviation = calculate_std_deviation(observations)
    n = len(observations)
    if n > 2:
        skewness = sum((x - mean) ** 3 for x in observations) / (n * std_deviation ** 3)
        return skewness
    return 0

# Function to calculate the kurtosis of the data
def calculate_kurtosis(observations):
    mean = calculate_mean(observations)
    std_deviation = calculate_std_deviation(observations)
    n = len(observations)
    if n > 3:
        kurtosis = sum((x - mean) ** 4 for x in observations) / (n * std_deviation ** 4) - 3
        return kurtosis
    return 0

# Function to calculate the 5-number summary
def calculate_five_number_summary(observations):
    observations.sort()
    n = len(observations)
    if n >= 4:
        q1_index = (n - 1) // 4
        q3_index = 3 * (n - 1) // 4
        q1 = observations[q1_index]
        q3 = observations[q3_index]
    else:
        q1 = q3 = observations[0]
    
    median = calculate_median(observations)
    min_value = observations[0]
    max_value = observations[-1]
    
    return min_value, q1, median, q3, max_value

# Main function
def main():
    print("Welcome to the Advanced Statistics Calculator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new dataset")
        print("2. Calculate statistics for a dataset")
        print("3. List existing datasets")
        print("4. Compare datasets")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

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
                print(f"Coefficient of Variation: {calculate_coeff_of_variation(observations)}%")
                print(f"Skewness: {calculate_skewness(observations)}")
                print(f"Kurtosis: {calculate_kurtosis(observations)}")
                min_val, q1, median, q3, max_val = calculate_five_number_summary(observations)
                print(f"5-Number Summary: Min={min_val}, Q1={q1}, Median={median}, Q3={q3}, Max={max_val}")
            else:
                print(f"Dataset '{dataset_name}' not found.")
        elif choice == '3':
            print("Existing datasets:")
            for name in datasets:
                print(name)
        elif choice == '4':
            if len(datasets) < 2:
                print("You need at least two datasets to compare.")
            else:
                print("Choose datasets to compare:")
                for i, name in enumerate(datasets.keys()):
                    print(f"{i + 1}. {name}")
                dataset_indices = input("Enter the numbers of the datasets to compare (e.g., 1 2): ").split()
                datasets_to_compare = [list(datasets[list(datasets.keys())[int(idx) - 1]]) for idx in dataset_indices]
                print("Comparison of selected datasets:")
                for i, dataset in enumerate(datasets_to_compare):
                    dataset_name = list(datasets.keys())[int(dataset_indices[i]) - 1]
                    print(f"Dataset '{dataset_name}':")
                    print(f"Mean: {calculate_mean(dataset)}")
                    print(f"Median: {calculate_median(dataset)}")
                    print(f"Mode: {calculate_mode(dataset)}")
                    print(f"Variance: {calculate_variance(dataset)}")
                    print(f"Standard Deviation: {calculate_std_deviation(dataset)}")
                    print(f"Coefficient of Variation: {calculate_coeff_of_variation(dataset)}%")
                    print(f"Skewness: {calculate_skewness(dataset)}")
                    print(f"Kurtosis: {calculate_kurtosis(dataset)}")
                    min_val, q1, median, q3, max_val = calculate_five_number_summary(dataset)
                    print(f"5-Number Summary: Min={min_val}, Q1={q1}, Median={median}, Q3={q3}, Max={max_val}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
