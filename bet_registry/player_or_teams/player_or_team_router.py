
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .player_or_team_repository import PlayerOrTeamRepository
from .player_or_team_schema import PlayerOrTeamGet

router = APIRouter(
  prefix="/player_or_team",
  tags=["player_or_team"],
  responses={404: {"description": "Not found betslip/s"}},
)

@router.get("/{player_or_team_id}", response_model=PlayerOrTeamGet)
def read_betslip(player_or_team_id: int, db = Depends(get_db)):
    betslip_repo = PlayerOrTeamRepository(db)
    return betslip_repo.get_player_or_team(player_or_team_id)

