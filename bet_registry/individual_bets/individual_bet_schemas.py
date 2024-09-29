from pydantic import BaseModel


class IndividualBetCreate(BaseModel):
    player_or_teams1_id: int
    player_or_teams2_id: int
    type_of_bet: str
    specific_bet: str
    bet_status_id: int
    league_or_tournaments_id: int
    odds: float