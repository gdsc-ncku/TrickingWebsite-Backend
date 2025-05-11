import jwt
import datetime
from fastapi import Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config import JWT_KEY
from exception import *

SECRET_KEY = JWT_KEY
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRES_IN = 30

SECURITY = HTTPBearer(
    scheme_name="JWT",
    description="JWT which get from /auth/login."
)


def generate_tokens(payload):
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {
        "access_token": access_token,
    }

def verify_jwt(token: HTTPAuthorizationCredentials = Security(SECURITY)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise TOKEN_EXPIRED
    except jwt.InvalidTokenError:
        raise TOKEN_INVALID
    
    
UserDepend = Depends(verify_jwt)
