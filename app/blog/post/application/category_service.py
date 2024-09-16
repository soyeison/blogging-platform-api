from app.blog.post.application.ports.category_repository import CategoryRepository
from app.blog.post.domain.category import CategoryEntity
from app.blog.post.infrastructure.schemas.post import PostSchema
from app.blog.post.infrastructure.schemas.post import PostCreateSchema
from app.blog.post.infrastructure.schemas.category import CategorySchema
from app.blog.post.infrastructure.schemas.category import CategoryCreateSchema

from app.database import Base, engine

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.categories = category_repository

    def getAll(self):
        pass
    
    def create(self, category: CategoryCreateSchema):
        try:
            category = self.categories.createCategory(category)

            category_schema = self.response_format(category)
            return category_schema.to_dict()
        except Exception as e:
            raise e
    
    def response_format(self, catgeory: CategoryEntity) -> CategorySchema:
        return CategorySchema(
            id=catgeory.id,
            name=catgeory.name
        )