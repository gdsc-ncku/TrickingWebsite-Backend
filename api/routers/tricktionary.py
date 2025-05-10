from fastapi import APIRouter

from schemas.trick import Trick

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
async def get_proficiency():
    return {"message": "meow"}

@router.put("/put_proficiency")
async def put_proficiency():
    return {"message": "meow"}