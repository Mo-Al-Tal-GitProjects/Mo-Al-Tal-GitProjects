def number_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_number(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    num = 0
    prev_value = 0
    for symbol in roman[::-1]:
        value = roman_dict[symbol]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value
    return num

def main():
    print("Roman Numerals Learning Assistant")
    print("---------------------------------")

    while True:
        print("\nOptions:")
        print("1. Convert Number to Roman Numeral")
        print("2. Convert Roman Numeral to Number")
        print("3. Learn Roman Numerals")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            try:
                user_input = int(input("Enter a number between 1 and 3999: "))
                if 1 <= user_input <= 3999:
                    roman_numeral = number_to_roman(user_input)
                    print(f"The Roman numeral for {user_input} is {roman_numeral}")
                else:
                    print("Please enter a number between 1 and 3999.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            user_input = input("Enter a Roman numeral: ")
            user_input = user_input.upper()
            if all(symbol in "IVXLCDM" for symbol in user_input):
                num = roman_to_number(user_input)
                print(f"The number for {user_input} is {num}")
            else:
                print("Invalid Roman numeral.")
        elif choice == "3":
            print("\nRoman Numerals Reference:")
            print("I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
