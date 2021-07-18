from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from API.Models import lost_item_model
from ..database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=50), unique=True, index=True)
    password = Column(String(length=50))

    lost_by_user_items = relationship("Item", foreign_keys="[Item.lost_by_user_id]",back_populates="lost_by_user")
    found_by_user_items = relationship("Item", foreign_keys="[Item.found_by_user_id]",back_populates="found_by_user")