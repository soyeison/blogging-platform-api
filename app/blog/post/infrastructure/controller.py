from fastapi import APIRouter, HTTPException, status
from typing import List
from fastapi.responses import JSONResponse
from app.blog.post.application.read_all_posts_use_case import ReadAllPostsUseCase
from app.blog.post.infrastructure.in_memory_post_repository import InMemoryPostRepository
from app.blog.post.infrastructure.models.post import PostModel

class PostController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.get("/", response_model=List[PostModel])(self.read_all_posts)

    async def read_all_posts(self):
        try:
            post_repository = InMemoryPostRepository()
            read_all_posts_use_case = ReadAllPostsUseCase(post_repository)
            content = read_all_posts_use_case.execute()

            return JSONResponse(content=content, status_code=200)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))