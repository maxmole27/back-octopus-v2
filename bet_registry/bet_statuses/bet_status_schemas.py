from datetime import datetime

from pydantic import BaseModel


class BetStatusBase(BaseModel):
    name: str
    description: str

class BetStatusGet(BetStatusBase):
    id: int
    class Config:
        from_attributes = True

# Here is no necessary list pagination, there are few statuses only