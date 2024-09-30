from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.blog.post.domain.post_tag import post_tag_association

class TagEntity(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    posts = relationship("PostEntity", secondary=post_tag_association, back_populates="tags")