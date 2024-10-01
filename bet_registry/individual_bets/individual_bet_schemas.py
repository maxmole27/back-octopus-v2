from datetime import datetime

from pydantic import BaseModel

from ..league_or_tournaments.league_or_tournament_schema import \
    LeagueOrTournamentGet
from ..player_or_teams.player_or_team_schema import PlayerOrTeamGet


class IndividualBetCreate(BaseModel):
    player_or_team1_id: int
    player_or_team2_id: int
    type_of_bet: str
    specific_bet: str
    bet_status_id: int
    league_or_tournament_id: int
    odds: float

class IndividualBetGet(IndividualBetCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    player_or_team1: PlayerOrTeamGet
    player_or_team2: PlayerOrTeamGet

    league_or_tournament: LeagueOrTournamentGet



    class Config:
        from_attributes = True