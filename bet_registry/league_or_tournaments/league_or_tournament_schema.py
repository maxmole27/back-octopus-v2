from typing import Optional

from pydantic import BaseModel


class LeagueOrTournamentBase(BaseModel):
    name: str
    description: str
    image_url: Optional[str]
    sport_id: int
    location_id: int
    alternative_name: Optional[str]
    alternative_name2: Optional[str]


class LeagueOrTournamentCreate(LeagueOrTournamentBase):
    pass

class LeagueOrTournamentGet(LeagueOrTournamentBase):
    id: int

    class Config:
        from_attributes = True