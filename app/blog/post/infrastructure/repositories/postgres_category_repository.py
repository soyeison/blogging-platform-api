from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from app.blog.post.domain.post import PostEntity
from app.blog.post.domain.category import CategoryEntity
from app.blog.post.infrastructure.schemas.category import CategoryCreateSchema
from app.blog.post.application.ports.post_repository import PostRepository
from app.blog.post.application.ports.category_repository import CategoryRepository

class PostgresCategoryRepository(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def createCategory(self, category: CategoryCreateSchema) -> CategoryEntity:
        try:
            db_category = CategoryEntity(
                name=category.name
            )
            self.db.add(db_category)
            self.db.commit()
            self.db.refresh(db_category)
            return db_category

        except Exception as e:
            raise e
    
    def readAllCategories(self) -> List[CategoryEntity]:
        pass
    
    def updateCategory(self):
        pass
    
    def deleteCategory(self):
        pass