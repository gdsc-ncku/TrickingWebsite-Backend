from pydantic import BaseModel

from beanie import Document

class CategoryBase(BaseModel):
    name: str
    description: str

class Category(CategoryBase, Document):
    pass

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass