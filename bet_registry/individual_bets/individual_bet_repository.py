from sqlalchemy.orm import Session

from .individual_bet_model import IndividualBet


class IndividualBetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, bet_data: dict) -> IndividualBet:
        new_individual_bet = IndividualBet(
            player_or_team1_id=bet_data.player_or_team1_id,
            player_or_team2_id=bet_data.player_or_team2_id,
            type_of_bet=bet_data.type_of_bet,
            specific_bet=bet_data.specific_bet,
            bet_status_id=bet_data.bet_status_id,
            league_or_tournament_id=bet_data.league_or_tournament_id,
            odds=bet_data.odds
        )
        self.db.add(new_individual_bet)
        self.db.flush()  # Flush para obtener el ID
        return new_individual_bet
