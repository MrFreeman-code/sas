# https://codelab.pro/kurs-po-fastapi-avtorizacziya-i-autentifikacziya-5/

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.db.pg.crud import users as crud_u


router = APIRouter(
    prefix="/a",
    tags=["Admin Only"],
)

@router.post("/users/")
def create_user(name: str, email: str, age: int, db: Session = Depends(get_db)):
    return crud_u.create_user(db, name, email, age)

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_u.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user
