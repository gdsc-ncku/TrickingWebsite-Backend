import time
from fastapi import APIRouter

from schemas.trick import Trick
from schemas.user import User
from schemas.proficiency import Proficiency, ProficiencyUpdate, ProficiencyPublic
from .utils.jwt import UserDepend
from exception import USER_NOT_EXISTS, TRICK_NOT_EXIST

STATUS_COMPLETE = 2


router = APIRouter()

@router.get("/get_all_trick")
async def get_all_trick():
    trick_list = await Trick.find_all().to_list()

    # I need to do this workaround because fetch_links=True doesn't 
    # work like it should with documents. 
    # This problem has existed for a long time. 
    # https://github.com/BeanieODM/beanie/issues/1011
    for trick in trick_list:
        await trick.fetch_link("difficulty_id")
        await trick.fetch_link("categories_id")

    return trick_list

@router.get("/get_proficiency")
async def get_proficiency(payload: UserDepend):
    user_id = payload['id']

    if not await User.get(user_id):
        return USER_NOT_EXISTS

    proficiency = await Proficiency.find_many(Proficiency.user_id == str(user_id)).\
                        project(ProficiencyPublic).to_list()

    return proficiency

@router.put("/put_proficiency")
async def put_proficiency(data: ProficiencyUpdate, payload: UserDepend):
    user_id = payload['id']
    trick_id = data.trick_id

    if not await User.get(user_id):
        return USER_NOT_EXISTS
    if not await Trick.get(trick_id):
        return TRICK_NOT_EXIST

    proficiency = await Proficiency.find_one(Proficiency.user_id == str(user_id), 
                                       Proficiency.trick_id == str(trick_id))
    if proficiency is None:
        pro_dict = data.model_dump()
        pro_dict['user_id'] = payload['id']
        if data.status == STATUS_COMPLETE: 
            pro_dict['completed_date'] = int(time.time())

        proficiency = Proficiency(**pro_dict)
        await Proficiency.insert_one(proficiency)
    else:
        proficiency.status = data.status
        if data.status == STATUS_COMPLETE and proficiency.completed_date is None:
            proficiency.completed_date = int(time.time())
        await proficiency.save()
    
    return proficiency.model_dump(include={"trick_id", "completed_date", "status"})