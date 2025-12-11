"""
App discription:
This is the main application file for the Passwords Manager.
It imports necessary functions from the Functions module and initializes the application.

"""

# Import necessary modules
import Functions

def main():
    print("Welcome to the Passwords Manager!")

    user = input("Enter username: ")
    password = input("Enter password: ")

    # Call the login function from Functions module
    if Functions.login(user, password):
        print("Login successful!")
        print("Application is running...")

        while True:
            choice = Functions.display_menu()
            if choice == '1':
                Functions.add_password()
            elif choice == '2':
                #this function for testing
                Functions.view_passwords()
            elif choice == '3':
                Functions.delete_password()
            elif choice == '4':
                Functions.logout()
                print("Exiting application. Goodbye!")
                break
            

if __name__ == "__main__":
    main()
    