from typing import Optional

from fastapi import APIRouter, Depends

from ...database import get_db
from .league_or_tournament_repository import LeagueOrTournamentRepository
from .league_or_tournament_schema import (LeagueOrTournamentCreate,
                                          LeagueOrTournamentGet,
                                          LeagueOrTournamentReadOrCreate)

router = APIRouter(
    prefix="/league_or_tournaments",
    tags=["league_or_tournaments"],
    responses={404: {"description": "Not found league_or_tournament/s"}},
)

@router.get("/by_sport/{sport_id}")
def read_league(db = Depends(get_db), sport_id: int = 0):
    league_or_tournament_repo = LeagueOrTournamentRepository(db)
    return league_or_tournament_repo.get_league_or_tournaments_by_sport_raw(sport_id=sport_id)

@router.get("/{league_or_tournament_id}")
def read_league(league_or_tournament_id: str, db = Depends(get_db)):
    league_or_tournament_repo = LeagueOrTournamentRepository(db)
    return league_or_tournament_repo.get_league_or_tournament(league_or_tournament_id)

@router.post("/")
def create_league(league_or_tournament: LeagueOrTournamentCreate, db = Depends(get_db)) :
    league_or_tournament_repo = LeagueOrTournamentRepository(db)
    return league_or_tournament_repo.create_league_or_tournament(league_or_tournament)

@router.post("/find_or_create")
def create_if_not_exists_league(body: LeagueOrTournamentReadOrCreate, db = Depends(get_db)) -> LeagueOrTournamentGet:
    league_or_tournament_repo = LeagueOrTournamentRepository(db)
    find_league_or_tournament = league_or_tournament_repo.get_league_or_tournaments_by_sport_raw(body.name, body.sport_id)
    if find_league_or_tournament:
        return find_league_or_tournament
    else:
        return league_or_tournament_repo.create_league_or_tournament(body.league_or_tournament)