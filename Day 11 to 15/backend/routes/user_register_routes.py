from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.user_model import UserModel
from schemas.user_schema import UserRegisterSchema
from service.user_service import hash_password
from repository.user_repository import (
    create_user_repo,
    get_user_by_email_repo,
    get_user_by_id_repo
)

user_router = APIRouter(tags=["User Authentication"])


# 1. User Registration API
@user_router.post('/register', status_code=status.HTTP_201_CREATED)
@user_router.post('/register-user', status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserRegisterSchema, db: Session = Depends(get_db)):
    # Check if email is already registered
    existing_user = get_user_by_email_repo(db=db, email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered. Please login or use a different email."
        )

    # Hash the password via the service layer
    hashed_pwd = hash_password(user_data.password)

    # Instantiate the SQLAlchemy UserModel
    user_model = UserModel(
        name=user_data.name,
        email=user_data.email,
        phonenumber=str(user_data.phonenumber),
        password=hashed_pwd
    )

    # Persist the record via the repository layer
    created_user = create_user_repo(db=db, user=user_model)

    return {
        "message": "User registered successfully",
        "id": created_user.id,
        "name": created_user.name,
        "email": created_user.email,
        "phonenumber": created_user.phonenumber,
        "created_at": created_user.created_at
    }


# 2. Get User Profile by ID
@user_router.get('/user/{user_id}')
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id_repo(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return {
        "message": "User fetched successfully",
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phonenumber": user.phonenumber,
        "created_at": user.created_at
    }
