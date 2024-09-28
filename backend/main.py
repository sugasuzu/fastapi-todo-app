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

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted"}
