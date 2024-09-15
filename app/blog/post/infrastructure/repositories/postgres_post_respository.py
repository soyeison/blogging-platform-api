from sqlalchemy.orm import Session
from datetime import datetime
from app.blog.post.domain.post import PostEntity
from app.blog.post.domain.category import CategoryEntity
from app.blog.post.infrastructure.schemas.post import PostCreateSchema
from app.blog.post.application.ports.post_repository import PostRepository

class PostgresPostRepository(PostRepository):
    def __init__(self, db: Session):
        self.db = db

    def readAllPosts(self) -> list[PostEntity]:
        try:
            posts = self.db.query(PostEntity).all()
            return posts
        except Exception as e:
            raise e
        
    def createPost(self, post: PostCreateSchema) -> PostEntity:
        try:
            # Consultar el id de la categoria
            category = self.db.query(CategoryEntity).filter(CategoryEntity.name == post.category).first()

            if category is None:
                raise Exception(f"The category {post.category} doesn't exist")
            
            db_post = PostEntity(
                title=post.title,
                content=post.content,
                categoryId=category.id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )
            self.db.add(db_post)
            self.db.commit()
            self.db.refresh(db_post)
            return db_post

        except Exception as e:
            raise e

    def updatePost(self):
        pass

    def deletePost(self):
        pass