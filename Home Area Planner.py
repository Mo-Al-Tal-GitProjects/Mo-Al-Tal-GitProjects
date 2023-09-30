class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class House:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, name, length, width):
        room = Room(name, length, width)
        self.rooms.append(room)
        print(f"Room '{name}' added successfully.")

    def list_rooms(self):
        print(f"\nRooms in '{self.name}':")
        for room in self.rooms:
            print(f"{room.name}: Length={room.length} ft, Width={room.width} ft, Area={room.area()} sq.ft")

    def total_area(self):
        total = sum(room.area() for room in self.rooms)
        return total

if __name__ == "__main__":
    print("House Area Calculator")
    house_name = input("Enter the name of your house: ")
    house = House(house_name)

    while True:
        print("\nOptions:")
        print("1. Add a Room")
        print("2. List Rooms")
        print("3. Calculate Total Area")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_name = input("Enter room name: ")
            length = float(input("Enter room length (in feet): "))
            width = float(input("Enter room width (in feet): "))
            house.add_room(room_name, length, width)
        elif choice == "2":
            house.list_rooms()
        elif choice == "3":
            total_area = house.total_area()
            print(f"Total area of '{house.name}' is {total_area:.2f} sq.ft")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
