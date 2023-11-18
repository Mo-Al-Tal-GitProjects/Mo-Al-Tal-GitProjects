import statistics
import scipy.stats as stats
import plotly.express as px
import pandas as pd

# Dictionary to store datasets
datasets = {}

# Function to calculate the mean
def calculate_mean(observations):
    return sum(observations) / len(observations)

# Function to calculate the 95% confidence interval
def calculate_confidence_interval(observations):
    mean = calculate_mean(observations)
    std_deviation = statistics.stdev(observations)
    n = len(observations)
    margin_of_error = 1.96 * (std_deviation / math.sqrt(n))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

# Function to perform a t-test for two datasets
def perform_t_test(dataset1, dataset2):
    t_statistic, p_value = stats.ttest_ind(dataset1, dataset2)
    return t_statistic, p_value

# Function to create an interactive histogram
def create_histogram(observations, dataset_name):
    df = pd.DataFrame({dataset_name: observations})
    fig = px.histogram(df, x=dataset_name, title=f'Histogram for {dataset_name}')
    fig.show()

# Main function
def main():
    print("Welcome to the Advanced Statistics Analyzer!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new dataset")
        print("2. Calculate statistics for a dataset")
        print("3. Perform a t-test between two datasets")
        print("4. Create an interactive histogram for a dataset")
        print("5. List existing datasets")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

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
                lower_bound, upper_bound = calculate_confidence_interval(observations)
                print(f"95% Confidence Interval: ({lower_bound}, {upper_bound})")
            else:
                print(f"Dataset '{dataset_name}' not found.")
        elif choice == '3':
            dataset1_name = input("Enter the name of the first dataset: ")
            dataset2_name = input("Enter the name of the second dataset: ")
            if dataset1_name in datasets and dataset2_name in datasets:
                t_statistic, p_value = perform_t_test(datasets[dataset1_name], datasets[dataset2_name])
                print(f"T-Statistic: {t_statistic}")
                print(f"P-Value: {p_value}")
                if p_value < 0.05:
                    print("The difference between the datasets is statistically significant (p < 0.05).")
                else:
                    print("There is no statistically significant difference between the datasets (p >= 0.05).")
            else:
                print("One or both of the datasets were not found.")
        elif choice == '4':
            dataset_name = input("Enter the name of the dataset: ")
            if dataset_name in datasets:
                create_histogram(datasets[dataset_name], dataset_name)
            else:
                print(f"Dataset '{dataset_name}' not found.")
        elif choice == '5':
            print("Existing datasets:")
            for name in datasets:
                print(name)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
