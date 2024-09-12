from typing import List

class PostDTO:
    def __init__(self, id: int, title: str, content: str, category: str, tags: List[str], createdAt: str, updatedAt: str) -> None:
        self.id = id
        self.title = title
        self.content: content
        self.category = category
        self.tags = tags
        self.createdAt = createdAt
        self.updatedAt = updatedAt
