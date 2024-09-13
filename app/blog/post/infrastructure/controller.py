from fastapi import APIRouter, HTTPException, status
from typing import List
from fastapi.responses import JSONResponse
from app.blog.post.infrastructure.repositories.in_memory_post_repository import InMemoryPostRepository
from app.blog.post.application.post_service import PostService
from app.blog.post.infrastructure.schemas.post import PostSchema

class PostController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.get("/", response_model=List[PostSchema])(self.read_all_posts)

    async def read_all_posts(self):
        try:
            post_repository = InMemoryPostRepository()
            post_service = PostService(post_repository)
            content = post_service.getAll()

            return JSONResponse(content=content, status_code=200)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))