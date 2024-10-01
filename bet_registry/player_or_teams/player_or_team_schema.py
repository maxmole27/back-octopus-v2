from typing import Optional

from pydantic import BaseModel

from ...shared.sports.sport_schemas import SportGet


class BasePlayerOrTeam(BaseModel):
    name: str
    alternative_name: Optional[str]
    alternative_name2: Optional[str]
    sport_id: int
    sport: SportGet

class PlayerOrTeamGet(BasePlayerOrTeam):
    id: int

    class Config:
        from_attributes = True