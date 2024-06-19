from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str

class RoleGet(RoleBase):
    id: int
    created_at: str
    updated_at: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleDelete():
    id: int
    class Config:
        orm_mode = True