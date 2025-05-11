from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import (
    MONGODB_URI,
    MONGODB_NAME,
    MONGODB_TLS,
    MONGODB_CAFILE
)
from schemas.trick import Trick
from schemas.category import Category
from schemas.diffculty import Difficulty
from schemas.user import User

client = AsyncIOMotorClient(
    MONGODB_URI,
    tls=MONGODB_TLS,
    tlsCAFile=MONGODB_CAFILE
)

DB = client[MONGODB_NAME]


async def setup():
    await init_beanie(
        database=DB,
        document_models=[
            Trick,
            Category,
            Difficulty,
            User
        ]
    )
