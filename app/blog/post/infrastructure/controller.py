from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.blog.post.infrastructure.repositories.postgres_post_respository import PostgresPostRepository
from app.blog.post.infrastructure.repositories.postgres_category_repository import PostgresCategoryRepository
from app.blog.post.application.post_service import PostService
from app.blog.post.application.category_service import CategoryService
from app.blog.post.infrastructure.schemas.post import PostSchema
from app.blog.post.infrastructure.schemas.post import PostCreateSchema
from app.blog.post.infrastructure.schemas.category import CategorySchema
from app.blog.post.infrastructure.schemas.category import CategoryCreateSchema

class PostController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.get("/", response_model=List[PostSchema])(self.read_all_posts)
        self.router.get("/seed")(self.seed_tables)
        self.router.post("/", response_model=PostSchema)(self.create_post)
        self.router.post("/category", response_model=CategorySchema)(self.create_category)

    async def read_all_posts(self, db: Session = Depends(get_db)):
        try:
            post_repository = PostgresPostRepository(db)
            post_service = PostService(post_repository)
            content = post_service.getAll()

            return JSONResponse(content=content, status_code=200)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    async def seed_tables(self, db: Session = Depends(get_db)):
        try:
            post_repository = PostgresPostRepository(db)
            post_service = PostService(post_repository)
            content = post_service.seed_tables()

            return JSONResponse(content=content, status_code=200)
        except Exception as e:
            raise e
    
    async def create_post(self, post: PostCreateSchema, db: Session = Depends(get_db)):
        try:
            post_repository = PostgresPostRepository(db)
            post_service = PostService(post_repository)
            content = post_service.create(post)

            return JSONResponse(content=content, status_code=201)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    async def create_category(self, post: CategoryCreateSchema, db: Session = Depends(get_db)):
        try:
            category_repository = PostgresCategoryRepository(db)
            category_service = CategoryService(category_repository)
            content = category_service.create(post)

            return JSONResponse(content=content, status_code=201)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))