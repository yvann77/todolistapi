from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.firebase import db

router = APIRouter()

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

@router.get("/todos", tags=["todos"])
def get_todos():
    todos = db.child("todos").get().val()
    return todos if todos else []

@router.post("/todos", tags=["todos"])
def create_todo(task: Task):
    new_todo = db.child("todos").push(task.dict())
    return {"id": new_todo["name"], **task.dict()}

@router.get("/todos/{todo_id}", tags=["todos"])
def get_todo(todo_id: str):
    todo = db.child("todos").child(todo_id).get().val()
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/todos/{todo_id}", tags=["todos"])
def update_todo(todo_id: str, task: Task):
    todo = db.child("todos").child(todo_id).get().val()
    if todo:
        db.child("todos").child(todo_id).update(task.dict())
        return {"id": todo_id, **task.dict()}
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{todo_id}", tags=["todos"])
def delete_todo(todo_id: str):
    todo = db.child("todos").child(todo_id).get().val()
    if todo:
        db.child("todos").child(todo_id).remove()
        return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")