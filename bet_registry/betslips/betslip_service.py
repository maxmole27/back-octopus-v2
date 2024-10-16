from typing import List

from sqlalchemy.orm import Session

from ..individual_bets.individual_bet_model import IndividualBetBetslip
from ..individual_bets.individual_bet_repository import IndividualBetRepository
from .betslip_model import Betslip
from .betslip_repository import BetslipGet, BetslipRepository
from .betslip_schemas import BetslipCreate


class BetslipService:
    def __init__(self, db: Session, betslip_repo: BetslipRepository, individual_bet_repo: IndividualBetRepository):
        self.db = db
        self.betslip_repo = betslip_repo
        self.individual_bet_repo = individual_bet_repo

    def create_betslip_with_individual_bets(self, betslip_data: BetslipCreate, individual_bets_data: List[dict]) -> BetslipGet:
        try:
            # Crear la Betslip
            new_betslip = self.betslip_repo.create(betslip_data)
            # Crear las IndividualBet y asociarlas a la Betslip
            for bet_data in individual_bets_data:
                new_individual_bet = self.individual_bet_repo.create(bet_data)

                # Crear la relación en la tabla intermedia
                individual_bet_betslip = IndividualBetBetslip(
                    individual_bet_id=new_individual_bet.id,
                    betslip_id=new_betslip.id
                )
                self.db.add(individual_bet_betslip)

            # Confirmar los cambios
            self.db.commit()
            self.db.refresh(new_betslip)

            return new_betslip
        except Exception as e:
            self.db.rollback()  # En caso de error, revertir los cambios
            raise e