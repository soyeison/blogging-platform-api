from app.blog.post.application.ports.tag_repository import TagRepository
from app.blog.post.domain.tag import TagEntity
from app.blog.post.infrastructure.schemas.post import PostSchema
from app.blog.post.infrastructure.schemas.post import PostCreateSchema
from app.blog.post.infrastructure.schemas.tag import TagCreateSchema, TagSchema

from app.database import Base, engine

class TagService:
    def __init__(self, tag_repository: TagRepository):
        self.tags = tag_repository

    def getAll(self):
        pass
    
    def create(self, tag: TagCreateSchema):
        try:
            tag = self.tags.createTag(tag)

            tag_schema = self.response_format(tag)
            return tag_schema.__dict__
        except Exception as e:
            raise e
    
    def response_format(self, tag: TagEntity) -> TagSchema:
        return TagSchema(
            id=tag.id,
            name=tag.name
        )