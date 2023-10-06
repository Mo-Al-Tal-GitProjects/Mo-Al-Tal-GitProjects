class DistanceTracker:
    def __init__(self):
        self.trips = []

    def calculate_distance(self, speed, total_time):
        return speed * total_time

    def record_trip(self, speed, total_time):
        distance = self.calculate_distance(speed, total_time)
        self.trips.append((speed, total_time, distance))

    def display_trip_logs(self):
        print("\nTrip Logs:")
        print("Trip  Speed (m/hr)  Time (hrs)  Distance (m)")
        print("-------------------------------------------")
        for i, trip in enumerate(self.trips, start=1):
            speed, total_time, distance = trip
            print(f"{i:<5}{speed:<16}{total_time:<12}{distance:<14}")

    def calculate_average_speed(self):
        total_speed = sum(trip[0] for trip in self.trips)
        total_time = sum(trip[1] for trip in self.trips)
        return total_speed / total_time

    def generate_trip_report(self):
        print("\nTrip Report:")
        print(f"Total Trips: {len(self.trips)}")
        print(f"Total Distance Traveled: {sum(trip[2] for trip in self.trips)} meters")
        print(f"Average Speed: {self.calculate_average_speed():.2f} m/hr")

def main():
    distance_tracker = DistanceTracker()

    while True:
        print("\nDistance Tracker Menu:")
        print("1. Record a Trip")
        print("2. Display Trip Logs")
        print("3. Generate Trip Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            speed = int(input("Enter vehicle speed in m/hr: "))
            total_time = int(input("Enter time taken to travel distance in hrs: "))
            distance_tracker.record_trip(speed, total_time)
            print("Trip recorded successfully!")

        elif choice == "2":
            distance_tracker.display_trip_logs()

        elif choice == "3":
            distance_tracker.generate_trip_report()

        elif choice == "4":
            print("Exiting Distance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
