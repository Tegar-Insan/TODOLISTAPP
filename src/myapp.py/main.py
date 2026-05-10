from module import User, UserList, create_user, login_user 
from typing import List, Optional
from pydantic import ValidationError
from module2 import Todolist, TodolistList, todolist, create_todolist, view_todolist
from pydantic import BaseModel, RootModel, Field
import json


def main(): 

    print("WELCOME TO DO LIST APP")   
    print("SIGN IN FIRST TO USE THE APP!")
    print ("DONT HAVE AN ACCOUNT? SIGN UP FIRST!")
    while True:
        print("1. Sign Up")
        print("2. Sign in")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_user()
            print("WELCOME TO THE APP!") 
        elif choice == "2":
            login_user()
            break
        elif choice == "3":
            print("Exiting the app, thank you.")
            break
        else:
            print("Invalid choice. Please try again.")
    
        
if __name__ == "__main__":
    main()