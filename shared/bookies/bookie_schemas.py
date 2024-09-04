from datetime import datetime
from typing import List

from pydantic import BaseModel


class BookieBase(BaseModel):
    name: str
    description: str

class BookieGet(BookieBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes=True

class BookieCreate(BookieBase):
    pass

class BookieDelete():
    id: int
    name: str

    class Config:
        from_attributes=True

class BookiesResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[BookieGet]
    message: str = None
    code: int = None
    