from fastapi import FastAPI


api = FastAPI()

# GET, POST, PUT DELETE
# GET - Retrieve information
# POST - Add new information
# PUT - Update existing information
# DELETE - Remove information
@api.get("/")
def index():
    return {"message": "Hello, World!"}

