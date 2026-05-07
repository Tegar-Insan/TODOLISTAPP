from module import create_user, login_user 


def main():    
    
    while True:
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()