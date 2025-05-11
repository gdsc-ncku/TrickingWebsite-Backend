from pydantic import BaseModel, Field
from uuid import UUID

from beanie import Document

class ProficiencyBase(BaseModel):
    user_id: UUID
    trick_id: UUID
    status: int = Field(ge=1, le=4, 
                        description="One user's proficiency status of a trick. \
                            1 is default, 2 is started, 3 is completed, 4 is proficient")
    
class ProficiencyCreate(ProficiencyBase):
    pass

class Proficiency(ProficiencyBase, Document):
    completed_date: int = Field(..., description="The complete time of a trick(UNIX timestamp, seconds from 1970-01-01)")


class ProficiencyUpdate(ProficiencyBase):
    pass
