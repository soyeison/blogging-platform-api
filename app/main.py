from fastapi import FastAPI
import uvicorn

from blog.post.application.read_all_posts_use_case import ReadAllPostsUseCase
from blog.post.infrastructure.in_memory_post_repository import InMemoryPostRepository
from blog.post.infrastructure.controller import PostController

def create_app():
    app = FastAPI()

    post_controller = PostController()

    app.include_router(post_controller.router, prefix="/posts", tags=["Post"])

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)