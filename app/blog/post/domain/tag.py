from typing import Optional
from dataclasses import dataclass

@dataclass
class Tag:
    name: str
    id: Optional[int] = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }