from abc import ABC, abstractmethod
from typing import List
from app.blog.post.infrastructure.dtos.post_dto import PostDTO

class PostRepository(ABC):
    @abstractmethod
    def createPost(self):
        pass

    @abstractmethod
    def readAllPosts(self) -> List[PostDTO]:
        pass

    @abstractmethod
    def updatePost(self):
        pass

    @abstractmethod
    def deletePost(self):
        pass