
from pydantic import BaseModel
from typing import Optional
from pydantic.schema import date

class ItemBase(BaseModel):
    name: str
    location: str
    lost_date: date
    lost_by_user_id: int
    is_found: bool
    found_date: date
    found_by_user_id: int

class ItemCreate(ItemBase):
    name: str
    location: str
    lost_date: date
    lost_by_user_id: int

class ItemUpdate(ItemBase):
    name: str
    location: str
    lost_date: date
    lost_by_user_id: int

class ItemDelete(BaseModel):
    lost_item_id :int

class Item(ItemBase):
    lost_item_id :int
    name: str
    location: str
    lost_date: date
    lost_by_user_id: int
    is_found: bool
    found_date: date
    found_by_user_id: int

    class Config:
        orm_mode = True