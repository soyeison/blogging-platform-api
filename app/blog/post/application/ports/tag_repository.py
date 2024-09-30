from abc import ABC, abstractmethod
from typing import List
from app.blog.post.domain.tag import TagEntity
from app.blog.post.infrastructure.schemas.tag import TagCreateSchema

class TagRepository(ABC):
    @abstractmethod
    def createTag(self, post: TagCreateSchema) -> TagEntity:
        pass

    @abstractmethod
    def readAllTags(self) -> List[TagEntity]:
        pass

    @abstractmethod
    def updateTag(self):
        pass

    @abstractmethod
    def deleteTag(self):
        pass