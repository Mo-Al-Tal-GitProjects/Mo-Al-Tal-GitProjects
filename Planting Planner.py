def calculate_plants(row_length, end_post_space, plant_spacing):
    available_space = row_length - (2 * end_post_space)
    num_plants = int(available_space / plant_spacing)
    return num_plants

def calculate_resources(num_plants, rows):
    total_plants = num_plants * rows
    total_wire_length = (total_plants - rows) * 2  # Each plant needs two wires
    total_posts = rows * 2  # Two posts per row
    return total_plants, total_wire_length, total_posts

if __name__ == "__main__":
    print("Planting Planner")
    print("----------------")

    while True:
        try:
            row_length = float(input("Enter the length of the row (in feet): "))
            end_post_space = float(input("Enter the space used by the end post (in feet): "))
            plant_spacing = float(input("Enter the space between plants (in feet): "))
            rows = int(input("Enter the number of rows: "))

            # Calculate the number of plants in a single row
            num_plants = calculate_plants(row_length, end_post_space, plant_spacing)

            # Calculate resources needed for the entire planting area
            total_plants, total_wire_length, total_posts = calculate_resources(num_plants, rows)

            # Display results
            print(f"Number of plants that fit in a single row: {num_plants}")
            print(f"Total number of plants in the planting area: {total_plants}")
            print(f"Total wire length needed (feet): {total_wire_length}")
            print(f"Total number of end posts required: {total_posts}")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break
