from typing import List, Optional
from pydantic import BaseModel
from API.Schemas.lost_item_schemas import Item

class UserBase(BaseModel):
    user_id: int
    email:str
    password :str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    password: str
    email: str

class User(UserBase):
    user_id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
