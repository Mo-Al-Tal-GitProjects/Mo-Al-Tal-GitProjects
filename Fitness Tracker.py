class FitnessTracker:
    def __init__(self):
        self.calories_burned = []
        self.workout_logs = []

    def calculate_calories_burned(self, duration):
        # Calculate calories burned based on a user's weight and exercise intensity
        weight = float(input("Enter your weight in kg: "))
        intensity = float(input("Enter the exercise intensity (MET value): "))
        calories = (0.035 * weight) * intensity * duration / 200

        self.calories_burned.append(calories)
        return calories

    def log_workout(self, duration, exercise_type):
        calories = self.calculate_calories_burned(duration)
        self.workout_logs.append((exercise_type, duration, calories))

    def display_workout_logs(self):
        print("Workout Logs:")
        for i, log in enumerate(self.workout_logs, start=1):
            exercise_type, duration, calories = log
            print(f"Log {i}: {exercise_type}, Duration: {duration} mins, Calories Burned: {calories:.2f} kcal")

    def generate_report(self):
        total_calories_burned = sum(self.calories_burned)
        total_duration = sum(log[1] for log in self.workout_logs)
        average_intensity = total_calories_burned / total_duration * 200 / float(input("Enter your weight in kg: "))

        print("\nFitness Report:")
        print(f"Total Calories Burned: {total_calories_burned:.2f} kcal")
        print(f"Total Workout Duration: {total_duration} mins")
        print(f"Average Exercise Intensity (MET value): {average_intensity:.2f} MET")

def main():
    fitness_tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Log a Workout")
        print("2. Display Workout Logs")
        print("3. Generate Fitness Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            exercise_type = input("Enter the exercise type: ")
            duration = int(input("Enter the workout duration in mins: "))
            fitness_tracker.log_workout(duration, exercise_type)
            print("Workout logged successfully!")

        elif choice == "2":
            fitness_tracker.display_workout_logs()

        elif choice == "3":
            fitness_tracker.generate_report()

        elif choice == "4":
            print("Exiting Fitness Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
