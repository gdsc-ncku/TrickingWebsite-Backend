from pydantic import BaseModel

from beanie import Document

class DifficultyBase(BaseModel):
    name: str
    description: str
    display_order: int

class Difficulty(DifficultyBase, Document):
    pass

class DifficultyCreate(DifficultyBase):
    pass

class DifficultyUpdate(DifficultyBase):
    pass