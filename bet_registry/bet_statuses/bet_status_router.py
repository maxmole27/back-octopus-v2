from fastapi import APIRouter, Depends

from ...database import get_db
from .bet_status_repository import BetStatusRepository
from .bet_status_schemas import BetStatusGet

router = APIRouter(
    prefix="/bet_statuses",
    tags=["bet_statuses"],
    responses={404: {"description": "Not found bet status/es"}},
)

@router.get("/raw", response_model=list[BetStatusGet])
def read_bet_statuses_raw(db = Depends(get_db)):
    bet_status_repo = BetStatusRepository(db)
    return bet_status_repo.get_bet_statuses_raw()

@router.get("/{bet_status_id}", response_model=BetStatusGet)
def read_bet_status(bet_status_id: int, db = Depends(get_db)):
    bet_status_repo = BetStatusRepository(db)
    return bet_status_repo.get_bet_status(bet_status_id)

