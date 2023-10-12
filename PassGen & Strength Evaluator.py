import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    length_score = min(len(password) / 12, 1)
    uppercase_score = 1 if any(char.isupper() for char in password) else 0
    number_score = 1 if any(char.isdigit() for char in password) else 0
    special_char_score = 1 if any(char in string.punctuation for char in password) else 0

    total_score = length_score + uppercase_score + number_score + special_char_score

    if total_score == 4:
        return "Very Strong"
    elif total_score >= 3:
        return "Strong"
    elif total_score >= 2:
        return "Moderate"
    elif total_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def save_password_to_file(password, filename):
    with open(filename, "a") as file:
        file.write(password + "\n")

def main():
    print("Password Generator and Strength Evaluator")
    print("-------------------------------------------")

    password_list = []

    num_passwords = int(input("Enter the number of passwords to generate: "))

    for _ in range(num_passwords):
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

        print("\nGenerated Password: ", password)
        strength = check_password_strength(password)
        print("Password Strength: ", strength)

        save_password = input("Do you want to save this password? (yes/no): ").lower()
        if save_password == "yes":
            password_list.append(password)

    filename = "saved_passwords.txt"
    for password in password_list:
        save_password_to_file(password, filename)

    print("Passwords saved to 'saved_passwords.txt'.")

if __name__ == "__main__":
    main()

