from typing import Optional
from dataclasses import dataclass

@dataclass
class Category:
    name: str
    id: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }