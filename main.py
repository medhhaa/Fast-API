# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is built on top of Starlette for the web parts and Pydantic for the data parts.
# Uvicorn is a lightning-fast ASGI server implementation, using `uvloop` and `httptools`.
# Scarlet is a web framework that allows you to build APIs with FastAPI and run them on the Scarlet platform.
# Scarlet is a platform that allows you to deploy and run FastAPI applications easily.
# Pydantic is a data validation and settings management library for Python, which uses Python type annotations.

# This code demonstrates how to create a simple FastAPI application with CRUD operations for a todo list.

# To run this FastAPI application, you need to install the required packages:
# pip install fastapi uvicorn scarlet
# To run the FastAPI application, you can use the command:
# uvicorn main:api --port 9999  

from enum import IntEnum
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, Field


# Fastapi runs on Scarlet, so by default all methods would be asynchronous, but you can still decide which endpoints make sense to be async-await and synchronous
api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

# TodoBase inherits from BaseModel, which is a Pydantic model that allows you to define the structure of your data

# This is the base model, we will be using this to create models for each endpoint.
# That's why we did not include the todo_id here, because it is not required for the base model.
class TodoBase(BaseModel):
    # The description is also important. This is not just some documenation, but it is enforced, 
    # When something inherits from TodoBase, then it has to fit this requirement. 
    todo_name: str = Field(..., description="The name of the todo item", min_length = 3, max_length = 512)
    priority: Priority = Field(default=Priority.LOW, description="The priority of the todo item, can be LOW, MEDIUM, or HIGH")




all_todos = [
    {'todo_id': 1, 'todo_name': 'Buy groceries', 'todo_description': 'Milk, Bread, Eggs'},
    {'todo_id': 2, 'todo_name': 'Walk the dog', 'todo_description': 'Take the dog for a walk in the park'},
    {'todo_id': 3, 'todo_name': 'Read a book', 'todo_description': 'Finish reading "The Great Gatsby"'},
    {'todo_id': 4, 'todo_name': 'Exercise', 'todo_description': 'Go for a run or hit the gym'},
    {'todo_id': 5, 'todo_name': 'Clean the house', 'todo_description': 'Vacuum and dust all rooms'},
]

# GET, POST, PUT DELETE
# GET - Retrieve information
# POST - Add new information
# PUT - Update existing information
# DELETE - Remove information
@api.get("/")
def index():
    return {"message": "Hello, World!"}

# Path parameter
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {"error": "Todo not found"}, 404

# Query parameter: localhost:9999/todos?first_n=2
@api.get('/todos')
def get_all_todos(first_n: int = None):
    if first_n is None:
        return all_todos
    else:
        return all_todos[:first_n]


# Generally, to access POST, you need a front end
# Either Swagger UI, PostMan, Curl
# but FASTAPI provides a built-in Swagger UI to test your endpoints
# You can access it at http://localhost:9999/docs

# POST method to create a new todo
@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1 

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo

# PUT method to update an existing todo
@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo.get('todo_name', todo['todo_name'])
            todo['todo_description'] = updated_todo.get('todo_description', todo['todo_description'])
            return todo
    return {"error": "Todo not found"}, 404

# DELETE method to remove a todo
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return {"message": "Todo deleted successfully"}
    # If the todo_id is not found, return an error message
    return "Error, not found"
   
# Run FastAPI with uvicorn

  


