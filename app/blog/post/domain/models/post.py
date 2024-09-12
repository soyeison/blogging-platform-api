from typing import List
from dataclasses import dataclass
from blog.post.domain.models.category import Category
from blog.post.domain.models.tag import Tag

@dataclass
class Post:
    title: str
    content: str
    category: Category
    tags: List[Tag]
    createdAt: str
    updatedAt: str
    id: int

    def to_dict(self):
        print(self.content)
        print(self.category)
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category.to_dict(),
            "tags": [tag.to_dict() for tag in self.tags],
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }