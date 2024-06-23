from typing import List, Optional

from sqlalchemy.orm import Session

from . import bookie_model, bookie_schemas


class BookieRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_bookie(self, user_id: int) -> Optional[bookie_model.Bookie]:
        return self.db.query(bookie_model.Bookie).filter(bookie_model.Bookie.id == user_id).first()

    def get_bookies(self, skip: int = 0, limit: int = 10) -> List[bookie_model.Bookie]:
        return self.db.query(bookie_model.Bookie).offset(skip).limit(limit).all()

    def get_bookies_raw(self) -> List[bookie_model.Bookie]:
        return self.db.query(bookie_model.Bookie).limit(200).all()
    
    def count_bookies(self):
        return self.db.query(bookie_model.Bookie).count()
    
    def create_bookie(self, bookie: bookie_schemas.BookieCreate) -> bookie_model.Bookie:
        db_bookie = bookie_model.Bookie(name=bookie.name, description=bookie.description)
        self.db.add(db_bookie)
        self.db.commit()
        self.db.refresh(db_bookie)
        return db_bookie
    
    def update_bookie(self, bookie: bookie_schemas.BookieCreate, bookie_id: int) -> bookie_model.Bookie:
        db_bookie = self.get_bookie(bookie_id)
        db_bookie.name = bookie.name
        db_bookie.description = bookie.description
        self.db.commit()
        self.db.refresh(db_bookie)
        return db_bookie
    
    def delete_bookie(self, bookie_id: int) -> bookie_model.Bookie:
        db_bookie = self.get_bookie(bookie_id)
        self.db.delete(db_bookie)
        self.db.commit()
        return db_bookie