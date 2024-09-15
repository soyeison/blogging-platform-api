from typing import List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class PostEntity(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    categoryId = Column(Integer, ForeignKey('category.id'), nullable=True)
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))
    updatedAt = Column(DateTime, default=datetime.now(timezone.utc))

    category = relationship("CategoryEntity")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category.to_dict(),
            "tags": [tag.to_dict() for tag in self.tags],
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }