from pydantic import BaseModel, Field
from typing import List

class PostSchemaBase(BaseModel):
    title: str = Field(..., examples=["Default title"])
    content: str = Field(..., examples=["Default content"])
    category: str = Field(..., examples=["Default category"])
    tags: List[str] = Field(..., examples=[["Tag 1", "Tag 2"]])

class PostSchema(PostSchemaBase):
    id: int = Field(..., examples=[1])
    createdAt: str = Field(..., examples=["2021-09-01T12:30:00Z"])
    updatedAt: str = Field(..., examples=["2021-09-01T12:30:00Z"])

    class Config:
        from_attributes = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "tags": self.tags,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    
class PostCreateSchema(PostSchemaBase):
    pass
