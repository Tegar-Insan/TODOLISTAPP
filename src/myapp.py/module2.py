import os
from pydantic import BaseModel, RootModel, Field
import json
from pydantic import ValidationError
from module import create_user, login_user 


class todolist(BaseModel):
    title: str
    description: str
    due_date: str
    status: str = Field(default="pending", description="Status of the task")

def create_todolist():
    user_name = True
    password_user = True

    if user_name and password_user:
        login_user()
    elif user_name and not password_user:
        print("Password is required.")

