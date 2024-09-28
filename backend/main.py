from fastapi import FastAPI
from pydantic import BaseModel

# Todoアイテムのモデル定義
class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False  # デフォルトはFalse（未完了）


app = FastAPI()

todos = []  # Todoアイテムを格納するリスト

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo

@app.post("/todos/complete/{todo_id}")
def complete_todo(todo_id: int):
    global todos
    for todo in todos:
        if todo.id == todo_id:
            todo.completed = True
            return {"message": "Todo marked as completed", "todo": todo}
    return {"error": "Todo not found"}, 404
    
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted"}
