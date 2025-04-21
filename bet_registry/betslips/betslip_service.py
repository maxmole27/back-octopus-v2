from typing import List

from sqlalchemy.orm import Session

from ..individual_bets.individual_bet_model import IndividualBetBetslip
from ..individual_bets.individual_bet_repository import IndividualBetRepository
from .betslip_model import Betslip
from .betslip_repository import BetslipRepository
from .betslip_schemas import BetslipCreate, BetslipGet, BetslipUpdateCompleted


class BetslipService:
    def __init__(self, db: Session, betslip_repo: BetslipRepository, individual_bet_repo: IndividualBetRepository):
        self.db = db
        self.betslip_repo = betslip_repo
        self.individual_bet_repo = individual_bet_repo

    def create_betslip_with_individual_bets(self, betslip_data: BetslipCreate, individual_bets_data: List[dict]):
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
        
    def update_betslip_with_individual_bets(self, betslip_data: BetslipUpdateCompleted) -> BetslipGet:
        individual_betslips = []
        # Actualizar la Betslip
        updated_betslip = self.betslip_repo.update_betslip(betslip_data)
        # Actualizar las IndividualBet asociadas a la Betslip
        for bet_data in betslip_data.individual_bets:
            if bet_data.id > -1:
                print("1.- UPDATE ··················· ······ ····· ····· ····· ····· ····· · · · · ")
                updated_bet = self.individual_bet_repo.update(bet_data.id, bet_data)
                individual_betslips.append(updated_bet)
            else:
                new_individual_bet = self.individual_bet_repo.create(bet_data)
                print("2.- CREATE ··················· ······ ····· ····· ····· ····· ····· · · · · ")
                print(new_individual_bet)
                individual_betslips.append(new_individual_bet)
        # TODO: A veces no se cambian las individual bets, por ende hay que validar eso antes de hacer el delete y renovar las relaciones
        # Eliminar las relaciones anteriores
        self.db.query(IndividualBetBetslip).filter(IndividualBetBetslip.betslip_id == betslip_data.betslip_id).delete()
        # Crear las nuevas relaciones
        for individual_bet in individual_betslips:
            # Crear la relación en la tabla intermedia
            individual_bet_betslip = IndividualBetBetslip(
                individual_bet_id=individual_bet.id,
                betslip_id=updated_betslip.id
            )
            self.db.add(individual_bet_betslip)
        # Confirmar los cambios
        self.db.commit()
        self.db.refresh(updated_betslip)
        print(updated_betslip)
        return updated_betslip