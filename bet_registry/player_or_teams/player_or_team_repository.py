from sqlalchemy.orm import Session

from .player_or_team_model import PlayerOrTeam
from .player_or_team_schema import PlayerOrTeamGet


class PlayerOrTeamRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_player_or_team(self, player_or_team_id: int) -> PlayerOrTeam:
    return self.db.query(PlayerOrTeam).filter(PlayerOrTeam.id == player_or_team_id).first()