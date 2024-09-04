from datetime import datetime
from typing import List

from pydantic import BaseModel


class SportBase(BaseModel):
    name: str
    description: str

class SportGet(SportBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes=True

class SportCreate(SportBase):
    pass

class SportDelete():
    id: int
    name: str

    class Config:
        from_attributes=True

class SportsResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[SportGet]
    message: str = None
    code: int = None
    