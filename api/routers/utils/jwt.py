from typing import Annotated
import jwt
import datetime
from fastapi import Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config import JWT_KEY
from exception import *
from schemas.user import User
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRES_IN = 30

SECURITY = HTTPBearer(
    scheme_name="JWT",
    description="JWT which get from /auth/login."
)


def generate_tokens(payload: User):
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    access_token = jwt.encode(payload, JWT_KEY, algorithm=ALGORITHM)
    return {
        "access_token": access_token,
    }

def verify_jwt(token: HTTPAuthorizationCredentials = Security(SECURITY)):
    try:
        payload = jwt.decode(token.credentials, JWT_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise TOKEN_EXPIRED
    except jwt.InvalidTokenError:
        raise TOKEN_INVALID
    
    
user_depend = Depends(verify_jwt)
UserDepend = Annotated[User, user_depend]
