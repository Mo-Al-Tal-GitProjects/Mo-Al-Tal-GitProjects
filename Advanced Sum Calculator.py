def calculate_sum(start, end):
    return sum(range(start, end + 1))

def calculate_sum_divisible_by(start, end, divisor):
    return sum(x for x in range(start, end + 1) if x % divisor == 0)

def calculate_sum_of_squares(start, end):
    return sum(x ** 2 for x in range(start, end + 1))

def calculate_sum_of_cubes(start, end):
    return sum(x ** 3 for x in range(start, end + 1))

def display_in_number_system(number, base):
    if base == 2:
        return bin(number)
    elif base == 8:
        return oct(number)
    elif base == 16:
        return hex(number)
    else:
        return f"Unsupported base: {base}"

if __name__ == "__main__":
    print("Advanced Sum Calculator")
    print("-----------------------")

    while True:
        try:
            print("Choose an option:")
            print("1. Calculate Sum of Numbers")
            print("2. Calculate Sum of Numbers Divisible by a Divisor")
            print("3. Calculate Sum of Squares of Numbers")
            print("4. Calculate Sum of Cubes of Numbers")
            print("5. Display Number in Different Base")
            print("6. Quit")

            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                print(f"Sum of numbers from {start} to {end}: {calculate_sum(start, end)}")

            elif choice == 2:
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                divisor = int(input("Enter the divisor: "))
                print(f"Sum of numbers divisible by {divisor} from {start} to {end}: {calculate_sum_divisible_by(start, end, divisor)}")

            elif choice == 3:
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                print(f"Sum of squares from {start} to {end}: {calculate_sum_of_squares(start, end)}")

            elif choice == 4:
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                print(f"Sum of cubes from {start} to {end}: {calculate_sum_of_cubes(start, end)}")

            elif choice == 5:
                number = int(input("Enter the number to display: "))
                base = int(input("Enter the base (2, 8, 16): "))
                print(f"{number} in base {base}: {display_in_number_system(number, base)}")

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a valid option (1-6).")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
