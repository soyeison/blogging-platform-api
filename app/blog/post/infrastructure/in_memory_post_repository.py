from typing import List
from app.blog.post.domain.post_repository import PostRepository
from blog.post.infrastructure.dtos.post_dto import PostDTO

class InMemoryPostRepository(PostRepository):
    def __init__(self):
        self.posts = [
            {
                "id": 1,
                "title": "My First Blog Post",
                "content": "This is the content of my first blog post.",
                "category": "Technology",
                "tags": ["Tech", "Programming"],
                "createdAt": "2021-09-01T12:00:00Z",
                "updatedAt": "2021-09-01T12:00:00Z"
            },
            {
                "id": 2,
                "title": "My Second Blog Post",
                "content": "This is the content of my second blog post.",
                "category": "Technology",
                "tags": ["Tech", "Programming"],
                "createdAt": "2021-09-01T12:30:00Z",
                "updatedAt": "2021-09-01T12:30:00Z"
            }
        ]

    def readAllPosts(self) -> List[PostDTO]:
        try:
            return self.posts
        except Exception as e:
            raise e
    
    def createPost(self):
        pass

    def updatePost(self):
        pass

    def deletePost(self):
        pass