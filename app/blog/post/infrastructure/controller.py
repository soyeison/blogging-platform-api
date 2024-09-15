from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.blog.post.infrastructure.repositories.postgres_post_respository import PostgresPostRepository
from app.blog.post.application.post_service import PostService
from app.blog.post.infrastructure.schemas.post import PostSchema
from app.blog.post.infrastructure.schemas.post import PostCreateSchema

class PostController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.get("/", response_model=List[PostSchema])(self.read_all_posts)
        self.router.post("/", response_model=PostSchema)(self.create_post)

    async def read_all_posts(self, db: Session = Depends(get_db)):
        try:
            post_repository = PostgresPostRepository(db)
            post_service = PostService(post_repository)
            content = post_service.getAll()

            return JSONResponse(content=content, status_code=200)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    async def create_post(self, post: PostCreateSchema, db: Session = Depends(get_db)):
        try:
            post_repository = PostgresPostRepository(db)
            post_service = PostService(post_repository)
            content = post_service.create(post)

            return JSONResponse(content=content, status_code=201)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))