import os
import json
from pydantic import BaseModel, RootModel, Field
from pydantic import ValidationError
from typing import List, Optional

class Todolist(BaseModel):
    title: str 
    description: str
    duedate: str
    status: str = Field(default="pending")

class TodolistList (RootModel):
    root: list[Todolist]


def todolist(): 
    print ("\n""""""""""WELCOME TO THE TODO LIST APP!""""""""""")
    print ("here you can create your own todo list and manage your tasks effectively.")
    print ("choose from the options below to get started:")
    print("1. Create a new task\n2. View your todo list\n3. Exit the app")

    choice = int(input("Enter your choice"))
    if choice > 0 :
        create_todolist(choice)
        view_todolist(choice)
    else : 
        print ("invalid option, try again")

    def create_todolist(choice):
        
        if choice == "1":
            input_title = input("What do you want to do: ")
            input_descrition = input("Describe your task: ")
            input_due_date = input("When is the deadline?: ")
            task = Todolist(title=input_title, description=input_description, duedate=input_due_date)    
            dumped = task.model_dump_json()
        
            with open("task.json","r") as f:
                content_todo_list= f.read()
    
            todolist_context = dumped
            key_list = list(todolist_context)

            new_content = ""

            if not os.path.exists("task.json"):
                new_content = "[" + (todolist_context.replace("}\n{", "},\n{")) + "]"
            elif os.path.exists("task.json") : 
                new_content  += (todolist_context.replace("}\n{", "},\n{")) 

        
            dataloads = json.loads(todolist_context)
            with open("task.json", "w" ) as e:
                json.dump(dataloads, e, indent=4)

            print("Task created succesfully!")


    def view_todolist(choice): 
        with open("task.json", "r") as f: 
            content = f.read()
            validate = todolist.model_validate_json(content)

        for task in validate :
            if choice == "2":
                print(task.title)
                print(task.description)
                print(task.due_date)
                print(task.status)
                break
            else: 
                print("Invalid choice. Please try again.") 
    

    def update_todolist(choice):
        with open("task.json", "r") as f:
            content_update = e
            return content_update  
            
    def delete_todolist(choice):
        with open("task.json", "r") as e:
            e.pop()


    def returning(choice):
        if choice == "3":
            main()



                
                