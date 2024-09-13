from app.blog.post.application.ports.post_repository import PostRepository
from app.blog.post.domain.post import Post
from app.blog.post.domain.category import Category
from app.blog.post.domain.tag import Tag
from app.blog.post.infrastructure.schemas.post import PostSchema

class PostService:
    def __init__(self, post_repository: PostRepository):
        self.posts = post_repository

    def getAll(self):
        try:
            # traer todos los posts
            posts = self.posts.readAllPosts()

            # Parsearlos a modelos del dominio
            post_domain = [self.to_domain(post) for post in posts]

            # Darles el formato de la respuesta
            posts_schema = [self.response_format(post) for post in post_domain]
            post_resp = [post.to_dict() for post in posts_schema]

            return post_resp
        except Exception as e:
            raise e
        
    def to_domain(self, post) -> Post:
        post_domain = Post(
            id=post["id"],
            title=post["title"],
            content=post["content"],
            category=Category(name=post["category"]),
            tags=post["tags"],
            createdAt=post["createdAt"],
            updatedAt=post["updatedAt"]
        )
        return post_domain
    
    def response_format(self, post: Post) -> PostSchema:
        return PostSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            category=post.category.name,
            tags=post.tags,
            createdAt=post.createdAt,
            updatedAt=post.updatedAt
        )