from pydantic import BaseModel, Field
from typing import Optional
from beanie import Document

class ProficiencyBase(BaseModel):
    trick_id: str
    status: int = Field(ge=1, le=3, 
                        description="One user's proficiency status of a trick. \
                            1 is started, 2 is completed, 3 is proficient")
    
class ProficiencyCreate(ProficiencyBase):
    pass

class ProficiencyUpdate(ProficiencyBase):
    pass

class ProficiencyPublic(ProficiencyBase):
    completed_date: Optional[int] = Field(None , description="The complete time of a trick(UNIX timestamp, seconds from 1970-01-01)")
    pass

class Proficiency(ProficiencyPublic, Document):
    user_id: str