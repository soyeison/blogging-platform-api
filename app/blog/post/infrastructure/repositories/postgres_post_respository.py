from sqlalchemy.orm import Session
from app.blog.post.domain.post import PostEntity
from app.blog.post.application.ports.post_repository import PostRepository

class PostgresPostRepository(PostRepository):
    def __init__(self, db: Session):
        self.db = db

    def readAllPosts(self):
        try:
            posts = self.db.query(PostEntity).all()
            print("posts:", posts)
            return posts
        except Exception as e:
            raise e
        
    def createPost(self):
        pass

    def updatePost(self):
        pass

    def deletePost(self):
        pass