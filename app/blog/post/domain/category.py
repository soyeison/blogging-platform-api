from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class CategoryEntity(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    posts = relationship("PostEntity", back_populates="category", uselist=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }