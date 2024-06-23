from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from ..roles.role_schemas import RoleGet


class UserBase(BaseModel):
    email: EmailStr
    name: str
    username: str
    
class UserGet(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    role_id: int
    role: RoleGet
    class Config:
        from_attributes=True

class UserCreate(UserBase):
    password: str
    role_id: int

class UserUpdate(UserBase):
    password: str
    role_id: int



class UserDelete():
    id: int


class UserResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[UserGet]
    message: str = None
    code: int = None
