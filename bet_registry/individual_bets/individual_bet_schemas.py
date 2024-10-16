from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ...shared.bookies.bookie_schemas import BookieGet
from ..bet_statuses.bet_status_schemas import BetStatusGet
from ..league_or_tournaments.league_or_tournament_schema import \
    LeagueOrTournamentGet
from ..player_or_teams.player_or_team_schema import PlayerOrTeamGet


class IndividualBetBase(BaseModel):
    bet_status_id: int
    event_date: Optional[datetime]
    odds: float
    league_or_tournament_id: Optional[int]
    player_or_team1_id: Optional[int]
    player_or_team2_id: Optional[int]
    specific_bet: str
    sport_id: int
    type_of_bet: str


class IndividualBetCreate(IndividualBetBase):
    # if ids are not provided, we can use these fields and create the entities
    player_or_team1_str: Optional[str]
    player_or_team2_str: Optional[str]
    league_or_tournament_str: Optional[str]

class IndividualBetGet(IndividualBetBase):
    id: int
    created_at: datetime
    updated_at: datetime

    player_or_team1: Optional[PlayerOrTeamGet]
    player_or_team2: Optional[PlayerOrTeamGet]

    league_or_tournament: LeagueOrTournamentGet
    bet_status: BetStatusGet




    class Config:
        from_attributes = True