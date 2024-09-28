from fastapi import FastAPI
from pydantic import BaseModel

# Todoアイテムのモデル定義
class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False  # デフォルトはFalse（未完了）


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}