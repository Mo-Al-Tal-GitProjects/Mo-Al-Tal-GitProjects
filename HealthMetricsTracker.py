import csv
import matplotlib.pyplot as plt
from datetime import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.health_data = []

    def add_health_data(self, date, diet, exercise, sleep, calories, water, steps, heart_rate):
        self.health_data.append({
            "date": date,
            "diet": diet,
            "exercise": exercise,
            "sleep": sleep,
            "calories": calories,
            "water": water,
            "steps": steps,
            "heart_rate": heart_rate
        })
    
    def save_data(self, filename):
        keys = self.health_data[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.health_data)

def add_health_data(user):
    date = input("Enter the date (YYYY-MM-DD): ")
    diet = input("Describe your diet for today: ")
    exercise = input("Describe your exercise routine for today: ")
    sleep = input("Enter your sleep duration in hours: ")
    calories = input("Enter your calorie intake for today: ")
    water = input("Enter your water intake in liters: ")
    steps = input("Enter the number of steps walked: ")
    heart_rate = input("Enter your average heart rate: ")

    user.add_health_data(date, diet, exercise, sleep, calories, water, steps, heart_rate)
    
def plot_sleep_data(user):
    dates = [entry['date'] for entry in user.health_data]
    sleep_hours = [float(entry['sleep']) for entry in user.health_data]

    plt.plot(dates, sleep_hours, marker='o')
    plt.title(f"Sleep Trend for {user.name}")
    plt.xlabel("Date")
    plt.ylabel("Sleep Hours")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_calorie_intake(user):
    dates = [entry['date'] for entry in user.health_data]
    calories = [int(entry['calories']) for entry in user.health_data]

    plt.plot(dates, calories, marker='o', color='red')
    plt.title(f"Calorie Intake Trend for {user.name}")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_water_intake(user):
    dates = [entry['date'] for entry in user.health_data]
    water = [float(entry['water']) for entry in user.health_data]

    plt.plot(dates, water, marker='o', color='blue')
    plt.title(f"Water Intake Trend for {user.name}")
    plt.xlabel("Date")
    plt.ylabel("Liters")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def weekly_average_steps(user):
    # Assuming data is entered daily and in chronological order
    steps = [int(entry['steps']) for entry in user.health_data]
    if len(steps) < 7:
        print("Not enough data for weekly analysis.")
        return

    weekly_avg = sum(steps[-7:]) / 7
    print(f"Weekly Average Steps: {weekly_avg:.2f}")

def weekly_average_sleep(user):
    sleep_hours = [float(entry['sleep']) for entry in user.health_data if 'sleep' in entry]
    if len(sleep_hours) < 7:
        print("Not enough data for weekly sleep analysis.")
        return

    weekly_avg_sleep = sum(sleep_hours[-7:]) / 7
    print(f"Weekly Average Sleep (hours): {weekly_avg_sleep:.2f}")

def weekly_average_calories(user):
    calorie_intake = [int(entry['calories']) for entry in user.health_data if 'calories' in entry]
    if len(calorie_intake) < 7:
        print("Not enough data for weekly calorie analysis.")
        return

    weekly_avg_calories = sum(calorie_intake[-7:]) / 7
    print(f"Weekly Average Calorie Intake: {weekly_avg_calories:.2f}")

def weekly_average_water(user):
    water_intake = [float(entry['water']) for entry in user.health_data if 'water' in entry]
    if len(water_intake) < 7:
        print("Not enough data for weekly water analysis.")
        return

    weekly_avg_water = sum(water_intake[-7:]) / 7
    print(f"Weekly Average Water Intake (liters): {weekly_avg_water:.2f}")

def weekly_average_heart_rate(user):
    heart_rates = [int(entry['heart_rate']) for entry in user.health_data if 'heart_rate' in entry]
    if len(heart_rates) < 7:
        print("Not enough data for weekly heart rate analysis.")
        return

    weekly_avg_heart_rate = sum(heart_rates[-7:]) / 7
    print(f"Weekly Average Heart Rate (bpm): {weekly_avg_heart_rate:.2f}")

def main():
    print("Welcome to the Personal Health and Fitness Tracker")
    user_name = input("Enter your name: ")
    user = User(user_name)

    while True:
        add_health_data(user)
        if input("Add more data? (yes/no): ").lower() != 'yes':
            break

    user.save_data(f"{user.name}_health_data.csv")

    # Visualization
    plot_sleep_data(user)
    plot_calorie_intake(user)
    plot_water_intake(user)

    # Data Analysis
    weekly_average_steps(user)
    weekly_average_steps(user)
    weekly_average_sleep(user)
    weekly_average_calories(user)
    weekly_average_water(user)
    weekly_average_heart_rate(user)



if __name__ == "__main__":
    main()
