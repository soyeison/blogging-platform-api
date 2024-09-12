from typing import Any, List
from blog.post.infrastructure.dtos.post_dto import PostDTO
from app.blog.post.domain.post_repository import PostRepository
from blog.post.domain.mappers.post_mapper import PostMapper
from blog.post.domain.models.post import Post
from blog.post.infrastructure.models.post import PostModel

class ReadAllPostsUseCase():
    def __init__(self, post_repository: PostRepository):
        self.posts = post_repository

    def execute(self):
        try:
            # traer todos los posts
            posts = self.posts.readAllPosts()

            # Parsearlos a modelos del dominio
            posts_domain = [PostMapper.to_domain(post) for post in posts]

            # Darles el formato de la respuesta
            posts_model_resp = self.response_format(posts_domain)
            post_resp = [post.to_dict() for post in posts_model_resp]

            return post_resp
        except Exception as e:
            raise e
    
    def response_format(self, posts: list[Post]) -> List[PostModel]:
        posts_resp = [post.to_dict() for post in posts]
        posts_resp_formated: List[PostModel] = []
        for post in posts_resp:
            post_resp_formated = PostModel(
                id=post["id"],
                title=post["title"],
                content=post["content"],
                category=post["category"]["name"],
                tags=[tag["name"] for tag in post["tags"]],
                createdAt=post["createdAt"],
                updatedAt=post["updatedAt"]
            )
            """ post_resp_formated =  {
                "id": post["id"],
                "title": post["title"],
                "content": post["content"],
                "category": post["category"]["name"],
                "tags": [tag["name"] for tag in post["tags"]],
                "createdAt": post["createdAt"],
                "updatedAt": post["updatedAt"]
            } """
            posts_resp_formated.append(post_resp_formated)
        
        return posts_resp_formated