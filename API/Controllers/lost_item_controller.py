from sqlalchemy.orm import Session
from fastapi import HTTPException
from API.Models import lost_item_model as models
from API.Schemas import lost_item_schemas

def get_lost_items(db: Session):
    return db.query(models.Item).filter(models.Item.is_found == False).all()


# this function creates if lost_item_id == 0 else updates record
def create_lost_item(db: Session, lost_item_schemas: lost_item_schemas.ItemCreate):
    if lost_item_schemas.lost_item_id == 0:
        db_lost_item = models.Item(
            name= lost_item_schemas.name,
            description= lost_item_schemas.description,
            lost_lattitude= lost_item_schemas.lost_lattitude,
            lost_longitude= lost_item_schemas.lost_longitude,
            lost_date=lost_item_schemas.lost_date,
            is_found= lost_item_schemas.is_found,
            user_id= lost_item_schemas.user_id,
            picture=lost_item_schemas.picture
        )
        db.add(db_lost_item)
        db.commit()
        db.refresh(db_lost_item)
        return db_lost_item
    else:
        print("update")
        _u = db.query(models.Item).filter(models.Item.lost_item_id == lost_item_schemas.lost_item_id).one_or_none()
        _u.name = lost_item_schemas.name
        _u.description = lost_item_schemas.description
        _u.lost_lattitude = lost_item_schemas.lost_lattitude
        _u.lost_longitude = lost_item_schemas.lost_longitude
        _u.lost_date = lost_item_schemas.lost_date
        _u.is_found = lost_item_schemas.is_found
        _u.user_id = lost_item_schemas.user_id
        _u.picture=lost_item_schemas.picture
        db.add(_u)
        db.commit()
        db.refresh(_u)
        return _u

# this function also updates, but item id has to be provided in params
def update_lost_item(db: Session, lost_item_id: int, lost_item_schemas: lost_item_schemas.ItemUpdate):
    _u = db.query(models.Item).filter(models.Item.lost_item_id == lost_item_id).one_or_none()
    # print("\n\nlost item schemas are \n\n", _u)
    if _u:
        _u.name = lost_item_schemas.name
        _u.description = lost_item_schemas.description
        _u.lost_lattitude = lost_item_schemas.lost_lattitude
        _u.lost_longitude = lost_item_schemas.lost_longitude
        _u.lost_date = lost_item_schemas.lost_date
        _u.is_found = lost_item_schemas.is_found
        _u.user_id = lost_item_schemas.user_id
        _u.picture = lost_item_schemas.picture
        db.add(_u)
        db.commit()
        db.refresh(_u)
        return _u
    raise HTTPException(status_code=404, detail="Not Found")

def delete_lost_item(db: Session, lost_item_id: int):
    delete = db.query(models.Item).filter(models.Item.lost_item_id == lost_item_id).first()
    if delete is None:
        raise HTTPException(status_code=404, detail="Not Found")
    db.delete(delete)
    db.commit()
    return {"lost_item_id" : lost_item_id, "message": 'Success'}
