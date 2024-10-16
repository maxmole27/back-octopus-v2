from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .sport_repository import SportRepository
from .sport_schemas import SportCreate, SportGet, SportsResponse

router = APIRouter(
  prefix="/sports",
  tags=["sports"],
  responses={404: {"description": "Sport Not found"}}
)

@router.get("/", response_model=SportsResponse)
def read_sports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sport_repo = SportRepository(db)
    sports = sport_repo.get_sports(skip=skip, limit=limit)
    sport_counter = sport_repo.count_sports()
    
    return SportsResponse(
        currentPage=(skip // limit) + 1,
        totalPages=(sport_counter // limit) + 1 if sport_counter % limit > 0 else sport_counter // limit,
        totalItems=sport_counter,
        data=sports,
        message="Sports retrieved successfully",
        code=0
    )

@router.get("/raw", response_model=List[SportGet])
def read_sports_raw(name: Optional[str] = None, db: Session = Depends(get_db)):
    sport_repo = SportRepository(db)
    if name is None:
        return sport_repo.get_sports_raw()
    return sport_repo.get_sports_raw(name=name)
        

@router.post("/", response_model=SportGet)
def create_sport(sport: SportCreate, db: Session = Depends(get_db)):
    sport_repo = SportRepository(db)
    return sport_repo.create_sport(sport)

@router.put("/{sport_id}", response_model=SportGet)
def update_sport(sport_id: int, sport: SportCreate, db: Session = Depends(get_db)):
    sport_repo = SportRepository(db)
    return sport_repo.update_sport(sport, sport_id)

@router.delete("/{sport_id}", response_model=SportGet)
def delete_sport(sport_id: int, db: Session = Depends(get_db)):
    sport_repo = SportRepository(db)
    return sport_repo.delete_sport(sport_id)