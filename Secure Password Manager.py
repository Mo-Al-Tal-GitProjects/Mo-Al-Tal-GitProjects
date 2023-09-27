import json

# Initialize an empty password database
passwords = {}

def save_passwords():
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def encrypt_password(password):
    # Simple XOR encryption (you should use a more secure encryption method)
    key = 0x55
    encrypted_password = ''.join([chr(ord(char) ^ key) for char in password])
    return encrypted_password

def decrypt_password(encrypted_password):
    # Simple XOR decryption
    key = 0x55
    decrypted_password = ''.join([chr(ord(char) ^ key) for char in encrypted_password])
    return decrypted_password

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    if website in passwords:
        print("Password for this website already exists.")
    else:
        encrypted_password = encrypt_password(password)
        passwords[website] = {"username": username, "password": encrypted_password}
        print("Password saved successfully.")
        save_passwords()

def get_password():
    website = input("Website: ")
    if website in passwords:
        username = passwords[website]["username"]
        encrypted_password = passwords[website]["password"]
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("Password not found.")

def change_credentials():
    website = input("Website: ")
    if website in passwords:
        print("Options:")
        print("1. Change Username")
        print("2. Change Password")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            new_username = input("New Username: ")
            passwords[website]["username"] = new_username
            print("Username changed successfully.")
        elif choice == "2":
            new_password = input("New Password: ")
            encrypted_password = encrypt_password(new_password)
            passwords[website]["password"] = encrypted_password
            print("Password changed successfully.")
        else:
            print("Invalid choice. Please select 1 or 2.")
    else:
        print("Website not found.")

if __name__ == "__main__":
    print("Password Manager")
    passwords = load_passwords()

    while True:
        print("\nOptions:")
        print("1. Add a Password")
        print("2. Get a Password")
        print("3. List All Passwords")
        print("4. Change Credentials")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("\nStored Passwords:")
            for website, data in passwords.items():
                print(f"Website: {website}, Username: {data['username']}, Password: {decrypt_password(data['password'])}")
        elif choice == "4":
            change_credentials()
        elif choice == "5":
            print("Goodbye!")
            save_passwords()
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
