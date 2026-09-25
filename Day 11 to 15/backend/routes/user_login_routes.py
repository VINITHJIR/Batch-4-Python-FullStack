from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import Optional

from core.database import get_db
from schemas.user_login_schema import UserLoginRequestSchema, UserLoginResponseSchema
from repository.user_login_repository import find_user_by_email_repo, find_user_by_id_repo
from service.user_service import verify_password
from service.jwt_service import create_access_token, decode_access_token

login_router = APIRouter(tags=["User Authentication"])


# 1. User Login API - Generates JWT Token
@login_router.post('/login', response_model=UserLoginResponseSchema)
@login_router.post('/login-user', response_model=UserLoginResponseSchema)
def login_user(credentials: UserLoginRequestSchema, db: Session = Depends(get_db)):
    # Step 1: Check if user exists with the provided email
    user = find_user_by_email_repo(db=db, email=credentials.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Step 2: Verify the plain password against stored hashed password
    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Step 3: Generate JWT access token with user claims
    token_payload = {
        "sub": user.email,
        "user_id": user.id,
        "name": user.name
    }
    jwt_token = create_access_token(data=token_payload)

    # Step 4: Return access token and user info
    return {
        "message": "Login successful",
        "access_token": jwt_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phonenumber": user.phonenumber
        }
    }


# 2. Token Verification API (Utility to test and validate JWT token)
@login_router.get('/verify-token')
def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header"
        )

    # Extract Bearer token
    parts = authorization.split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format. Expected: 'Bearer <token>'"
        )

    token = parts[1]
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or has expired"
        )

    return {
        "message": "Token is valid",
        "data": payload
    }
