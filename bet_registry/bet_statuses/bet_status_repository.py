
from typing import List

from .bet_status_model import BetStatus
from .bet_status_schemas import BetStatusGet


class BetStatusRepository:
    def __init__(self, db):
        self.db = db

    def get_bet_status(self, bet_status_id: int) -> BetStatusGet:
        return self.db.query(BetStatus).filter(BetStatus.id == bet_status_id).first()
    
    def get_bet_statuses_raw(self) -> List[BetStatus]:
        return self.db.query(BetStatus).all()