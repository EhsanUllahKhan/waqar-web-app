from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship


from pydantic import BaseModel

from ..database import Base


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=20))
    location = Column(String(length=500))
    lost_date = Column(Date)
    lost_by_user_id = Column(Integer, ForeignKey("users.user_id"))
    is_found=Column(Boolean)
    found_by_user_id = Column(Integer, ForeignKey("users.user_id"))
    found_date = Column(Date)

    lost_by_user = relationship("User",foreign_keys="Item.lost_by_user_id",  back_populates="lost_by_user_items")
    found_by_user = relationship("User", foreign_keys="Item.found_by_user_id", back_populates="found_by_user_items")