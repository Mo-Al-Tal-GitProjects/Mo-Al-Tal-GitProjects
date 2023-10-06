import time

class RunningTracker:
    def __init__(self):
        self.runs = []
        self.shoe_mileage = 0

    def record_run(self):
        distance = float(input("Enter the distance of your run (in kilometers): "))
        duration = float(input("Enter the duration of your run (in minutes): "))
        terrain = input("Enter the terrain type (e.g., road, trail, track): ")
        weather = input("Enter the weather conditions: ")
        temperature = float(input("Enter the temperature (in Celsius): "))
        heart_rate = int(input("Enter your average heart rate (bpm): "))
        run_date = time.strftime("%Y-%m-%d %H:%M:%S")

        run_data = {
            "Distance (km)": distance,
            "Duration (min)": duration,
            "Terrain": terrain,
            "Weather": weather,
            "Temperature (C)": temperature,
            "Heart Rate (bpm)": heart_rate,
            "Date": run_date
        }

        self.runs.append(run_data)
        self.shoe_mileage += distance  # Add distance to shoe mileage
        print("Run recorded successfully!")

    def calculate_average_pace(self, run):
        duration = run["Duration (min)"]
        distance = run["Distance (km)"]
        pace_min = duration / distance
        return pace_min

    def display_run_logs(self):
        if not self.runs:
            print("No runs recorded yet.")
            return

        print("\nRun Logs:")
        for i, run in enumerate(self.runs, start=1):
            print(f"\nRun {i}:")
            for key, value in run.items():
                print(f"{key}: {value}")
            print(f"Average Pace (min/km): {self.calculate_average_pace(run):.2f}")

    def track_shoe_mileage(self):
        print(f"Total Shoe Mileage: {self.shoe_mileage} km")

    def set_running_goal(self):
        distance_goal = float(input("Set a distance goal (in kilometers): "))
        print(f"Your distance goal is set to {distance_goal} km.")

def main():
    running_tracker = RunningTracker()

    while True:
        print("\nRunning Tracker Menu:")
        print("1. Record a Run")
        print("2. Display Run Logs")
        print("3. Track Shoe Mileage")
        print("4. Set Running Goal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            running_tracker.record_run()

        elif choice == "2":
            running_tracker.display_run_logs()

        elif choice == "3":
            running_tracker.track_shoe_mileage()

        elif choice == "4":
            running_tracker.set_running_goal()

        elif choice == "5":
            print("Exiting Running Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
