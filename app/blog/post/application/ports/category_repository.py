from abc import ABC, abstractmethod
from typing import List
from app.blog.post.domain.category import CategoryEntity
from app.blog.post.infrastructure.schemas.category import CategoryCreateSchema

class CategoryRepository(ABC):
    @abstractmethod
    def createCategory(self, post: CategoryCreateSchema) -> CategoryEntity:
        pass

    @abstractmethod
    def readAllCategories(self) -> List[CategoryEntity]:
        pass

    @abstractmethod
    def updateCategory(self):
        pass

    @abstractmethod
    def deleteCategory(self):
        pass