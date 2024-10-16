from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ...shared.location.location_schema import LocationGet


class LeagueOrTournamentBase(BaseModel):
    name: str
    image_url: Optional[str]
    sport_id: int
    location_id: int
    alternative_name: Optional[str]
    alternative_name2: Optional[str]
    location: Optional[LocationGet]


class LeagueOrTournamentCreate(LeagueOrTournamentBase):
    pass

class LeagueOrTournamentGet(LeagueOrTournamentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class LeagueOrTournamentReadOrCreate(BaseModel):
    name: Optional[str]
    sport_id: Optional[int]
    league_or_tournament: LeagueOrTournamentCreate