from fastapi import HTTPException

USER_ALREADY_EXISTS = HTTPException(
    status_code=400,
    detail="The account is already exist"
)

USER_NOT_EXISTS = HTTPException(
    status_code=400,
    detail="The account is not exist"
)

WRONG_ACCOUNT_OR_PASSWORD = HTTPException(
    status_code=400,
    detail="wrong email or phone number or password"
)
TOKEN_EXPIRED = HTTPException(
    status_code=400, 
    detail="token expired"
)
TOKEN_INVALID = HTTPException(
    status_code=400, 
    detail="token invalid"
)
INSUFFICIENT_PERMISSIONS = HTTPException(
    status_code=400, 
    detail="insufficient permissions"
)

TRICK_NOT_EXIST = HTTPException(
    status_code=400, 
    detail="trick not exist"
)