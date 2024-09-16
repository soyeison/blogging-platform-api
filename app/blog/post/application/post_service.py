from app.blog.post.application.ports.post_repository import PostRepository
from app.blog.post.domain.post import PostEntity
from app.blog.post.infrastructure.schemas.post import PostSchema
from app.blog.post.infrastructure.schemas.post import PostCreateSchema
from app.database import Base, engine

class PostService:
    def __init__(self, post_repository: PostRepository):
        self.posts = post_repository

    def getAll(self):
        try:
            # traer todos los posts (Que estan como modelos del dominio)
            posts = self.posts.readAllPosts()

            # Darles el formato de la respuesta
            posts_schema = [self.response_format(post) for post in posts]
            post_resp = [post.to_dict() for post in posts_schema]

            return post_resp
        except Exception as e:
            raise e
        
    def seed_tables(self):
        try:
            ## Crear las tablas de la db
            Base.metadata.create_all(bind=engine)
            
            return {"message": "Table created successfully"}
        except Exception as e:
            raise e
    
    def create(self, post: PostCreateSchema):
        try:
            post = self.posts.createPost(post)

            post_schema = self.response_format(post)
            return post_schema.to_dict()
        except Exception as e:
            raise e
    
    def response_format(self, post: PostEntity) -> PostSchema:
        return PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            category=post.category.name,
            tags=["tasg1", "tag2"],
            createdAt=post.createdAt.strftime('%m/%d/%Y'),
            updatedAt=post.updatedAt.strftime('%m/%d/%Y')
        )