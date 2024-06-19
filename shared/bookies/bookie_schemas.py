from pydantic import BaseModel


class BookieBase(BaseModel):
    name: str
    description: str

class BookieList(BookieBase):
    id: int

class BookieCreate(BookieBase):
    pass

class BookieDelete():
    id: int
    name: str

    class Config:
        orm_mode = True