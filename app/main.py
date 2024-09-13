from fastapi import FastAPI

from app.config import settings

from app.blog.post.infrastructure.controller import PostController

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

post_controller = PostController()

app.include_router(post_controller.router, prefix="/posts", tags=["Post"])