from fastapi import APIRouter
from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from API.Schemas import lost_item_schemas as schemas
from API.Controllers import  lost_item_controller as crud
from ..database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


items = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@items.post("/", response_model=schemas.Item)
def create_Item(Item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_lost_item(db=db, lost_item_schemas=Item)

@items.get("/", response_model=List[schemas.Item])
def read_lost_items( db: Session = Depends(get_db)):
    lost_item = crud.get_lost_items(db)
    return lost_item 

@items.delete("/{lost_item_id}")
def read_lost_item(lost_item_id: int, db: Session = Depends(get_db)):
    db_lost_item = crud.delete_lost_item(db, lost_item_id=lost_item_id)
    if db_lost_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return {'msg':'Deleted'}
