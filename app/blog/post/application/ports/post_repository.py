from abc import ABC, abstractmethod
from typing import List
from app.blog.post.domain.post import PostEntity
from app.blog.post.infrastructure.schemas.post import PostCreateSchema

class PostRepository(ABC):
    @abstractmethod
    def createPost(self, post: PostCreateSchema) -> PostEntity:
        pass

    @abstractmethod
    def readAllPosts(self) -> List[PostEntity]:
        pass

    @abstractmethod
    def updatePost(self):
        pass

    @abstractmethod
    def deletePost(self):
        pass