from orjson import dumps, loads, OPT_INDENT_2
from pydantic import BaseModel

from os import urandom
from typing import Optional


class MongoDBConfig(BaseModel):
    uri: str = "mongodb://username:password@example.com/hspc"
    db_name: str = "hspc"
    use_tls: bool = False
    tls_cafile: Optional[str] = None


class Config(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    jwt_key: str = urandom(16).hex()
    allow_origins: list[str] = []
    mongodb_config: MongoDBConfig = MongoDBConfig()


if __name__ == "config":
    try:
        with open("config.json", "rb") as config_file:
            config = Config(**loads(config_file.read()))
    except:
        config = Config()

    HOST = config.host
    PORT = config.port
    JWT_KEY = config.jwt_key
    ALLOW_ORIGINS = config.allow_origins

    MONGODB_URI = config.mongodb_config.uri
    MONGODB_NAME = config.mongodb_config.db_name
    MONGODB_TLS = config.mongodb_config.use_tls
    MONGODB_CAFILE = config.mongodb_config.tls_cafile

    with open("config.json", "wb") as config_file:
        config_file.write(dumps(config.model_dump(), option=OPT_INDENT_2))
