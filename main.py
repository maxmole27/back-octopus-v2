from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import database
from .shared.bookies import bookie_model
from .shared.bookies.bookie_repository import BookieRepository
from .shared.bookies.bookie_schemas import (BookieCreate, BookieDelete,
                                            BookieList)

bookie_model.Base.metadata.create_all(bind=database.engine)


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/bookies", response_model=List[BookieList])
def read_bookies(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    bookie_repo = BookieRepository(db)
    bookies = bookie_repo.get_bookies(skip=skip, limit=limit)
    return bookies

@app.post("/bookies", response_model=BookieList)
def create_bookie(bookie: BookieCreate, db: Session = Depends(database.get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.create_bookie(bookie)

@app.put("/bookies/{bookie_id}", response_model=BookieList)
def update_bookie(bookie_id: int, bookie: BookieCreate, db: Session = Depends(database.get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.update_bookie(bookie, bookie_id)

@app.delete("/bookies/{bookie_id}", response_model=BookieList)
def delete_bookie(bookie_id: int, db: Session = Depends(database.get_db)):
    bookie_repo = BookieRepository(db)
    return bookie_repo.delete_bookie(bookie_id)