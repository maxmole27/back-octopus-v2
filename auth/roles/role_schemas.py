from datetime import datetime

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str

class RoleGet(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleDelete():
    id: int
    class Config:
        from_attributes=True