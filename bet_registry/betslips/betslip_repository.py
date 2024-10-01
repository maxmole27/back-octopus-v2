
from typing import List

from sqlalchemy.orm import Session, joinedload

from ..individual_bets.individual_bet_model import IndividualBet
from ..systems.system_model import System
from .betslip_model import Betslip
from .betslip_schemas import BetslipCreate, BetslipGet, BetslipResponse


class BetslipRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, betslip_data: BetslipCreate) -> Betslip:
        new_betslip = Betslip(
            system_id=betslip_data.system_id
        )
        self.db.add(new_betslip)
        self.db.flush()  # Flush para obtener el ID de betslip
        return new_betslip

    def get_betslip(self, betslip_id: int) -> Betslip:
        return self.db.query(Betslip).filter(Betslip.id == betslip_id).first()
    
    def get_betslips(self, page: int, limit: int) -> List[Betslip]:
        return self.db.query(Betslip).offset(page * limit).limit(limit).all()
    
    def get_betslips_from_system(self, system_id: int, page: int, limit: int) -> List[Betslip]:
        betslips = self.db.query(Betslip).filter(Betslip.system_id == system_id).offset(page*limit).limit(limit).all()
        return betslips
    
    def create_betslip(self, betslip: BetslipCreate) -> Betslip:
        db_betslip = Betslip(system_id=betslip.system_id)
        self.db.add(db_betslip)
        self.db.commit()
        self.db.refresh(db_betslip)
        return betslip
    
    def insert_betslip(self, betslip: Betslip) -> Betslip:
        individual_bet = IndividualBet()
        individual_bet.bet_status = "pending"
        individual_bet.type_of_bet = "single"
        individual_bet.specific_bet = 1.5
        individual_bet.odds = 2
        individual_bet.player_or_team1_id = 1
        individual_bet.player_or_team2_id = 2
        individual_bet.league_or_tournament_id = 1

        self.db.add(betslip)
        self.db.commit()
        self.db.refresh(betslip)
      
        return betslip
    
    def count_betslips(self, system_id: int) -> int:
        return self.db.query(Betslip).filter(Betslip.system_id == system_id).count()
    
