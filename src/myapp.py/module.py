import os
import json
from pydantic import BaseModel, RootModel, field_validator
from pydantic import ValidationError
from module2 import Todolist, TodolistList, todolist, create_todolist, view_todolist
from typing import List, Optional



class User(BaseModel):
    username: str
    password: str
    age : int



class UserList (RootModel):
    root: list[User]


def create_user():
    name_user = input("What is your name? ")
    password_user = input("What is your password? ")
    age_user = int(input("What is your age? "))


    user = User(username=name_user, password=password_user, age=age_user)
    datalist = user.model_dump_json()

    
    with open("users.json", "r") as f: 
        content = f.read()
    
    
    user_content = ""

    if not os.path.exists("users.json") or content == "":
        user_content = "[" + (content.replace("}\n{", "},\n{")) + "]"
    elif os.path.exists("users.json") and content != "":
        user_content += (content.replace("}\n{", "},\n{")) 


    data=json.loads(user_content)
    with open ("users.json", "w") as f:
        data.append(user.model_dump()) 
        json.dump(data, f, indent=4)

    while False:
        if name_user == "":
            print("Username is required.")
        elif password_user == "":
            print("Password is required.") 
        elif name_user == "" or password_user == "":
            raise ValueError("Both username and password are required.")  
        elif age_user < 18:
            print("You must be at least 18 years old to create an account.")

    
def login_user():

    while True:
        name_user = input("What is your name? ")
        password_user = input("What is your password? ") 
        with open('users.json', 'r') as f:
            raw_data = f.read()
    
        user_data = UserList.model_validate_json(raw_data).root
        db = UserList(root=user_data)
        user_found = None
        try: 
            for user in user_data:
                if  name_user == user.username and password_user == user.password:
                    user_found = UserList (root=[user])
                    user_found = True
                    print (f"Login sucessfull, welcome back {name_user}")
                    todolist()
                    break
            else:
                print("invalid password and username\n try again")

        except(ValidationError, ValueError, PermissionError) as e:
            print(f"ERROR MADAFAKA{e}")
          

      
    

    

    



    
 
        
        
    
