from fastapi import FastAPI

# Fastapi runs on Scarlet, so by default all methods would be asynchronous, but you can still decide which endpoints make sense to be async-await and synchronous

api = FastAPI()

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

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {"error": "Todo not found"}, 404

@api.get('/todos')
def get_all_todos(first_n = None):
    if first_n is None:
        return all_todos
    else:
        return all_todos[:first_n]

  


