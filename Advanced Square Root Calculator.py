import math

def calculate_square_root(number):
    return math.sqrt(number)

def calculate_nth_root(number, n):
    return number ** (1/n)

def is_perfect_square(number):
    root = int(math.sqrt(number))
    if root * root == number:
        return root
    return None

def calculate_square_roots_in_range(start, end, decimal_places):
    for x in range(start, end + 1):
        square_root = round(calculate_square_root(x), decimal_places)
        print(f"Square root of {x}: {square_root}")

if __name__ == "__main__":
    print("Advanced Square Root Calculator")
    print("--------------------------------")

    while True:
        try:
            print("Choose an option:")
            print("1. Calculate Square Root")
            print("2. Calculate nth Root")
            print("3. Check if a Number is a Perfect Square")
            print("4. Calculate Square Roots in a Range")
            print("5. Quit")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                number = float(input("Enter the number: "))
                print(f"Square root of {number}: {calculate_square_root(number)}")

            elif choice == 2:
                number = float(input("Enter the number: "))
                n = float(input("Enter the value of n: "))
                print(f"{n}th root of {number}: {calculate_nth_root(number, n)}")

            elif choice == 3:
                number = int(input("Enter the number: "))
                root = is_perfect_square(number)
                if root is not None:
                    print(f"{number} is a perfect square, its square root is: {root}")
                else:
                    print(f"{number} is not a perfect square.")

            elif choice == 4:
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                decimal_places = int(input("Enter the number of decimal places: "))
                calculate_square_roots_in_range(start, end, decimal_places)

            elif choice == 5:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a valid option (1-5).")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
