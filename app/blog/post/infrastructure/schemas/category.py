from pydantic import BaseModel, Field

class CategorySchemaBase(BaseModel):
    name: str = Field(..., examples=["tecnology"])

class CategorySchema(CategorySchemaBase):
    id: int = Field(..., examples=[1])

    class Config:
            from_attributes = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class CategoryCreateSchema(CategorySchemaBase):
    pass