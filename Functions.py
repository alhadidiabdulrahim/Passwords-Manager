import hashlib
import json
import os

def hash_password(password):
    # Function to hash a password
    return hashlib.sha256(password.encode()).hexdigest()


import json
import os

def login(user, password):
    # If volt.json doesn't exist → login fails
    if not os.path.exists("volt.json"):
        print("No user database found.")
        return False

    # Load stored passwords
    try:
        with open("volt.json", "r") as file:
            content = file.read().strip()
            data = json.loads(content) if content else {}
    except json.JSONDecodeError:
        print("Invalid volt.json file.")
        return False

    # Check if the username exists
    if user not in data:
        print("User not found.")
        return False

    # Hash the entered password
    hashed_input = hash_password(password)

    # Compare hashed passwords
    if data[user] == hashed_input:
        return True
    else:
        return False

def display_menu():
    # Function to display the main menu
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Delete Password")
    print("4. Exit")
    choice = input("Select an option: ")
    return choice

def add_password():
    site = input("Enter the site name: ")
    password = input("Enter the password: ")
    print(f"Password for {site} added successfully.")

    hashed_password = hash_password(password)

    # Ensure file exists and load data safely
    if not os.path.exists("volt.json"):
        data = {}
    else:
        with open("volt.json", "r") as file:
            try:
                content = file.read().strip()
                data = json.loads(content) if content else {}
            except json.JSONDecodeError:
                data = {}

    # Add new entry
    data[site] = hashed_password

    # Save updated JSON
    with open("volt.json", "w") as file:
        json.dump(data, file, indent=4)

def view_passwords():
    print("Displaying all stored passwords...")

    # Check if file exists
    if not os.path.exists("volt.json"):
        print("No passwords stored.")
        return

    # Try loading JSON
    try:
        with open("volt.json", "r") as file:
            content = file.read().strip()
            data = json.loads(content) if content else {}
    except (json.JSONDecodeError, FileNotFoundError):
        print("No passwords stored.")
        return

    # Empty dictionary?
    if not data:
        print("No passwords stored.")
        return

    # Print stored entries
    for site, hashed_password in data.items():
        print(f"Site: {site}, Hashed Password: {hashed_password}")

def delete_password():
    site = input("Enter the site name to delete: ")

    if not os.path.exists("volt.json"):
        print("No passwords stored.")
        return

    try:
        with open("volt.json", "r") as f:
            data = json.loads(f.read().strip() or "{}")
    except json.JSONDecodeError:
        print("Password file is corrupted.")
        return

    if site not in data:
        print(f"No password found for site '{site}'.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the password for '{site}'? (y/n): ").lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return

    # Delete the password
    del data[site]

    with open("volt.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Password for site '{site}' deleted successfully.")

def logout():
    print("Logging out...")
    print("Exiting application. Goodbye!")
    exit()  # stops the program

