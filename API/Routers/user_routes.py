from fastapi import APIRouter
from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from API.Schemas import user_schemas as schemas
from API.Controllers import  user_controller as crud
from ..database import SessionLocal

# was not able to import this function, so in a hurry wrote it here.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router_user = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router_user.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router_user.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login_user(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {'msg': 'login successful'}

@router_user.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users
