from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Request Schema for Login Authentication
class UserLoginRequestSchema(BaseModel):
    email: EmailStr = Field(..., description="Registered user email address")
    password: str = Field(..., min_length=1, description="Account password")


# User detail dictionary in token response
class UserDetailSchema(BaseModel):
    id: int
    name: str
    email: str
    phonenumber: Optional[str] = None


# Response Schema returning JWT Token and user info
class UserLoginResponseSchema(BaseModel):
    message: str
    access_token: str
    token_type: str = "bearer"
    user: UserDetailSchema
