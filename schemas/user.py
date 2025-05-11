from pydantic import BaseModel, Field

from beanie import Document

class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    password: str
    email: str
    sex: bool = Field(..., description="True is women, false is men")
    age: int
    

class UserCreate(UserBase):
    pass

class User(UserBase, Document):
    identity: int = Field(..., description="1 is student, 2 is teacher, 3 is manager")
    pass

class UserUpdate(UserBase):
    pass
