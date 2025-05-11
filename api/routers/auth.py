import time

import bcrypt
from fastapi import APIRouter

from exception import *
from schemas.user import UserCreate, User
from .utils.jwt import *

router = APIRouter()

@router.post('/register')
async def register(data: UserCreate):
    hashpw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    user_dict = data.model_dump()
    user_dict['password'] = hashpw.decode("utf-8")
    user_dict['role'] = user_dict['level'] = 1  #default setting
    user_dict['created_at'] = user_dict['updated_at'] = int(time.time())

    if await User.find_one(User.email == data.email) or \
        await User.find_one(User.phone_number == data.phone_number):
        return USER_ALREADY_EXISTS
    jwt_token = generate_tokens(user_dict)

    await User.insert_one(User(**user_dict))

    return jwt_token

async def login(user: User, password: str):
    if not user:
        return WRONG_ACCOUNT_OR_PASSWORD
    if not bcrypt.checkpw(password.encode(), user.password.encode("utf-8")):
        return WRONG_ACCOUNT_OR_PASSWORD
    
    user_dict = user.model_dump()
    user_dict.pop("id", None)

    return generate_tokens(user_dict)

@router.get('/email_login')
async def email_login(email: str, password: str):
    user = await User.find_one(User.email == email)
    return await login(user, password)

@router.get('/phone_login')
async def phone_login(phone_number: str, password: str):
    user = await User.find_one(User.phone_number == phone_number)
    return await login(user, password)