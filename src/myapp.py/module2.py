import os
from pydantic import BaseModel, RootModel, Field
import json
from pydantic import ValidationError
from typing import List, Optional

class Todolist(BaseModel):
    title: str 
    description: str
    duedate:int | str
    status: str = Field(default="pending")

class TodolistList (RootModel):
    root: list[Todolist]


def todolist(): 
    print ("\n"""""""""""WELCOME TO THE TODO LIST APP!""""""""""")
    print ("here you can create your own todo list and manage your tasks effectively.")
    print ("choose from the options below to get started:")
    print("1. Create a new task\n2. View your todo list\n3. Exit the app")
    choice = input("Enter your choice: ")
    create_todolist(choice)
    view_todolist(choice)

def create_todolist(choice):
    if choice == "1":
        input_title = input("What do you want to do: ")
        input_description = input("Describe your task: ")
        input_due_date = int(input("When is the deadline?: "))
        task = Todolist(title=input_title, description=input_description, duedate=input_due_date)    
        dumped = task.model_dump_json()
        
    with open("task.json","r") as f:
        content_todo_list= f.read()
    
    
    if not os.path.exists("task.json"):        
        content_todo_list = []

    else:
        content_todo_list += dumped
        dataloads = json.loads(content_todo_list) 

    with open("task.json","w") as e:
        dataloads.append(task.model_dump())
        e.write(content_todo_list)
        json.dump(content_todo_list ,e, indent=4)
  
    return e
    print("Task created succesfully!")
   
   
def view_todolist(choice): 
    with open("task.json", "r") as f: 
        content = f.read()
        validate = Todolist.model_validate_json(content)

    for task in validate.root:
        if choice == "2":
            print(task.title)
            print(task.description)
            print(task.due_date)
            print(task.status)
            break
    else: 
        print("Invalid choice. Please try again.") 
   

    if choice == "3":
        print("Exiting the app.")
        main()
    

        

                
                