from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from . import sport_model, sport_schemas


class SportRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_sport(self, user_id: int) -> Optional[sport_model.Sport]:
        return self.db.query(sport_model.Sport).filter(sport_model.Sport.id == user_id).first()

    def get_sports(self, skip: int = 0, limit: int = 10) -> List[sport_model.Sport]:
        return self.db.query(sport_model.Sport).offset(skip).limit(limit).all()

    def get_sports_raw(self, name: Optional[str] = None) -> List[sport_model.Sport]:
        query = self.db.query(sport_model.Sport)
        if name:
            query = query.filter(sport_model.Sport.name.ilike(f"%{name}%"))

        return query.limit(200).all()
    
    
    def count_sports(self):
        return self.db.query(sport_model.Sport).count()
    
    def create_sport(self, sport: sport_schemas.SportCreate) -> sport_model.Sport:
        db_sport = sport_model.Sport(name=sport.name, description=sport.description)
        self.db.add(db_sport)
        self.db.commit()
        self.db.refresh(db_sport)
        return db_sport
    
    def update_sport(self, sport: sport_schemas.SportCreate, sport_id: int) -> sport_model.Sport:
        db_sport = self.get_sport(sport_id)
        db_sport.name = sport.name
        db_sport.description = sport.description
        self.db.commit()
        self.db.refresh(db_sport)
        return db_sport
    
    def delete_sport(self, sport_id: int) -> sport_model.Sport:
        db_sport = self.get_sport(sport_id)
        self.db.delete(db_sport)
        self.db.commit()
        return db_sport