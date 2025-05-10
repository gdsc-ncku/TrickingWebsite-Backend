from pydantic import Field, BaseModel
from typing import Optional, List

from beanie import Document, Link

from .category import Category
from .diffculty import Difficulty

class TrickBase(BaseModel):
    name: str = Field(..., description="Name of the trick")
    description: str = Field(..., description="Description of the trick")
    prerequisites: bool = Field(..., description="prerequisites")
    GIF_path: Optional[str] = Field(..., description="gif path")


class Trick(TrickBase, Document):
    difficulty_id: Link[Difficulty]
    categories_id: List[Link[Category]]

class TrickCreate(TrickBase):
    difficulty_name: str
    category_names: List[str]
    
class TrickUpdate(TrickCreate):
    pass