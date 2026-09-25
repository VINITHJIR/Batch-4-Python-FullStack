from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Union
from datetime import datetime

# Schema for incoming user registration request
class UserRegisterSchema(BaseModel):
    name: str = Field(..., min_length=2, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid user email address")
    phonenumber: Union[int, str] = Field(..., description="User contact phone number")
    password: str = Field(..., min_length=6, description="Password with minimum 6 characters")

# Schema for user registration response
class UserResponseSchema(BaseModel):
    message: str
    id: int
    name: str
    email: str
    phonenumber: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
