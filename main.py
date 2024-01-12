from fastapi import FastAPI
from models import Todo
app = FastAPI()

@app.get('/')
async def root():
    return {'message' : 'HEllo World'}

todos = []

# get all todos
@app.get('/todos')
async def get_todos():
    return {'todos' : todos}

# get single todo
@app.get('/get/{id}')
async def get_todo(id : int):
    for todo in todos:
        if todo.id == id:
            return {'id' : todo.id,
                    'message' : todo.item
                    }
    return {'message' : 'todo not found'}
# create a todo@app.get('/todos')

# add a todo
@app.post("/post")
async def create_todo(todo : Todo):
    # todo : str -> means that the todo is of datatype string
    todos.append(todo)
    return {'message' : f'{todo.id} has been added'}

# update a todo
@app.put("/update/{todo_id}")
async def update_todo(todo_id : int, new_todo : Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = new_todo.item
            return {'message' : 'Todo has been updated!'}
            break
    return {'message' : 'Error: Todo not found'}




# delete a todo
@app.delete('/delete/{id}')
async def delete(id : int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {'message' : f' todo item \'{id}\' has been deleted'}
    return {'message' : 'todo not found'}

