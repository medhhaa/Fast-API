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


  


