from pydantic import BaseModel, Field

class TagSchemaBase(BaseModel):
    name: str = Field(..., examples=["Tech"])

class TagSchema(TagSchemaBase):
    id: int = Field(..., examples=[1])

    class Config:
        from_attributes = True

class TagCreateSchema(TagSchemaBase):
    pass