from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from app.blog.post.domain.post import PostEntity
from app.blog.post.domain.tag import TagEntity
from app.blog.post.infrastructure.schemas.tag import TagCreateSchema
from app.blog.post.application.ports.tag_repository import TagRepository

class PostgresTagRepository(TagRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def createTag(self, tag: TagCreateSchema) -> TagEntity:
        try:
            db_tag = TagEntity(
                name=tag.name
            )
            self.db.add(db_tag)
            self.db.commit()
            self.db.refresh(db_tag)
            return db_tag

        except Exception as e:
            raise e
    
    def readAllTags(self) -> List[TagEntity]:
        pass
    
    def updateTag(self):
        pass
    
    def deleteTag(self):
        pass