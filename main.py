from fastapi import FastAPI

# Fastapi runs on Scarlet, so by default all methods would be asynchronous, but you can still decide which endpoints make sense to be async-await and synchronous

api = FastAPI()

todos[] = [
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

@api.get('/calculation')
def calculation():


