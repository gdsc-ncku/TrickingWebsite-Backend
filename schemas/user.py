from pydantic import BaseModel, Field

from beanie import Document

class Date(BaseModel):
    year: int
    month: int = Field(ge=1, le=12)
    day: int = Field(ge=1, le=31)

class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    email: str
    phone_number: str
    password: str
    birtheday: Date
    avatar: str = Field(..., description="url of avatar")
    sex: bool = Field(..., description="True is women, False is men")
    
class UserCreate(UserBase):
    pass

class User(UserBase, Document):
    role: int = Field(ge=1, le=3, description="Role of the user. 1 is normal User, 2 is Admin, 3 is SuperAdmin")
    level: int = Field(ge=1, le=3, description="Identity card level of the user. 1 is blank, 2 is beginner, 3 is advanced")
    created_at: int = Field(..., description="The create time of the account(UNIX timestamp, seconds from 1970-01-01)")
    updated_at: int = Field(..., description="The last update time(UNIX timestamp, seconds from 1970-01-01)")

class UserUpdate(UserBase):
    pass

class EmailLogin(BaseModel):
    email: str
    password: str

class PhoneLogin(BaseModel):
    phone_number: str
    password: str