from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .bookie_repository import BookieRepository
from .bookie_schemas import BookieCreate, BookieList, BookiesResponse

router = APIRouter(
  prefix="/bookies",
  tags=["bookies"],
  responses={404: {"description": "Bookie Not found"}}
)

@router.get("/", response_model=BookiesResponse)
def read_bookies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bookie_repo = BookieRepository(db)
    bookies = bookie_repo.get_bookies(skip=skip, limit=limit)
    bookie_counter = bookie_repo.count_bookies()
    
    return BookiesResponse(
        currentPage=(skip // limit) + 1,
        totalPages=(bookie_counter // limit) + 1 if bookie_counter % limit > 0 else bookie_counter // limit,
        totalItems=bookie_counter,
        data=bookies,
        message="Bookies retrieved successfully",
        code=0
    )

@router.get("/raw", response_model=List[BookieList])
def read_bookies_raw(db: Session = Depends(get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.get_bookies_raw()

@router.post("/", response_model=BookieList)
def create_bookie(bookie: BookieCreate, db: Session = Depends(get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.create_bookie(bookie)

@router.put("/{bookie_id}", response_model=BookieList)
def update_bookie(bookie_id: int, bookie: BookieCreate, db: Session = Depends(get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.update_bookie(bookie, bookie_id)

@router.delete("/{bookie_id}", response_model=BookieList)
def delete_bookie(bookie_id: int, db: Session = Depends(get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.delete_bookie(bookie_id)