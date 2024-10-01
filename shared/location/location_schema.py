from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str
    flag: str
    code: str
    is_country: bool

class LocationCreate(LocationBase):
    pass

class LocationGet(LocationBase):
    id: int

    class Config:
        from_attributes = True