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

from fastapi import FastAPI, HTTPException
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
    todo_description: str = Field(..., description="The description of the todo item")
    priority: Priority = Field(default=Priority.LOW, description="The priority of the todo item, can be LOW, MEDIUM, or HIGH")

class TodoCreate(TodoBase):
    # It has no major difference from TodoBase, except that it is used for creating a new todo item.
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="The unique identifier for the todo item") 
    pass

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, description="The name of the todo item", min_length = 3, max_length = 512)
    todo_description: Optional[str] = Field(None, description="The description of the todo item", min_length = 3, max_length = 1024)
    priority: Optional[Priority] = Field(None, description="The priority of the todo item, can be LOW, MEDIUM, or HIGH")


all_todos = [
    Todo(todo_id = 1, todo_name = "Buy groceries", todo_description = "Milk, Bread, Eggs", priority = Priority.HIGH),
    Todo(todo_id = 2, todo_name = "Walk the dog", todo_description = "Take the dog for a walk in the park", priority = Priority.MEDIUM),     
    Todo(todo_id = 3, todo_name = "Read a book", todo_description = "Finish reading 'The Great Gatsby'", priority = Priority.LOW),
    Todo(todo_id = 4, todo_name = "Exercise", todo_description = "Go for a run or hit the gym", priority = Priority.MEDIUM),
    Todo(todo_id = 5, todo_name = "Clean the house", todo_description = "Vacuum and dust all rooms", priority = Priority.LOW)
]

# GET, POST, PUT DELETE
# GET - Retrieve information
# POST - Add new information
# PUT - Update existing information
# DELETE - Remove information

# Path parameter
@api.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code = 404, detail = "Todo not found")

# Query parameter: localhost:9999/todos?first_n=2
@api.get('/todos', response_model=List[Todo])
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

# response model is essentially, what are you returning
# but error strings may not be the same as your response model
# so you raise HTTPExceptions instead

# Typing
@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1 

    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )

    all_todos.append(new_todo)

    return new_todo

# PUT method to update an existing todo
@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code = 404, detail = "Todo not found")

# DELETE method to remove a todo
@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return {"message": "Todo deleted successfully"}
    # If the todo_id is not found, return an error message
    raise HTTPException(status_code = 404, detail = "Todo not found")
   
# Run FastAPI with uvicorn

  


