from app.blog.post.domain.models.post import Post
from app.blog.post.domain.models.category import Category
from app.blog.post.domain.models.tag import Tag
from app.blog.post.infrastructure.dtos.post_dto import PostDTO

class PostMapper:
    @staticmethod
    def to_domain(post_data: PostDTO) -> Post:
        return Post(
            id=post_data["id"],
            title=post_data["title"],
            content=post_data["content"],
            category=Category(post_data["category"]),
            tags=[Tag(tag_name) for tag_name in post_data["tags"]],
            createdAt=post_data["createdAt"],
            updatedAt=post_data["updatedAt"]
        )