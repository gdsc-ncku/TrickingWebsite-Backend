from fastapi import APIRouter

from schemas.trick import Trick

router = APIRouter()

@router.get("/get_all_trick")
async def get_all_trick():
    trick_list = await Trick.find_all(fetch_links=True).to_list()
    return trick_list

@router.get("/get_proficiency")
async def get_proficiency():
    return {"message": "meow"}

@router.put("/put_proficiency")
async def put_proficiency():
    return {"message": "meow"}