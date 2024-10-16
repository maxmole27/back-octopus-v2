from sqlalchemy.orm import Session

from ..league_or_tournaments.league_or_tournament_model import \
    LeagueOrTournament
from ..player_or_teams.player_or_team_model import PlayerOrTeam
from .individual_bet_model import IndividualBet


class IndividualBetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, bet_data: dict) -> IndividualBet:
        # find id of player_or_team1_id and player_or_team2_id
        # if not found, create the entity

        if bet_data.player_or_team1_id is None or bet_data.player_or_team1_id == -1:
            # create the entity, but first, we have to check if string name is already in the database
            check_if_exists_player1 = self.db.query(PlayerOrTeam).filter(
                PlayerOrTeam.name == bet_data.player_or_team1_str).filter(PlayerOrTeam.sport_id == bet_data.sport_id).first()
            if check_if_exists_player1 is not None:
                print('check_if_exists_player1', check_if_exists_player1.name)
                bet_data.player_or_team1_id = check_if_exists_player1.id
            else:
                new_player_or_team1 = PlayerOrTeam(
                name=bet_data.player_or_team1_str,
                    sport_id=bet_data.sport_id
                )
                self.db.add(new_player_or_team1)
                self.db.flush()
                bet_data.player_or_team1_id = new_player_or_team1.id
            
        if bet_data.player_or_team2_id is None or bet_data.player_or_team2_id == -1:
            # create the entity but first, we have to check if string name is already in the database
            # TODO: check alternative names too
            check_if_exists_player2 = self.db.query(PlayerOrTeam).filter(PlayerOrTeam.sport_id == bet_data.sport_id).filter(
                PlayerOrTeam.name == bet_data.player_or_team2_str).first()

            if check_if_exists_player2 is not None:
                bet_data.player_or_team2_id = check_if_exists_player2.id
            else:
                new_player_or_team2 = PlayerOrTeam(
                    name=bet_data.player_or_team2_str,
                    sport_id=bet_data.sport_id
                )
                self.db.add(new_player_or_team2)
                self.db.flush()
                bet_data.player_or_team2_id = new_player_or_team2.id

        if bet_data.league_or_tournament_id is None or bet_data.league_or_tournament_id == -1:
            # create the entity
            check_if_exists_torunament = self.db.query(LeagueOrTournament).filter(
                LeagueOrTournament.name == bet_data.league_or_tournament_str).filter(
                LeagueOrTournament.sport_id == bet_data.sport_id).first()
            if check_if_exists_torunament is not None:
                bet_data.league_or_tournament_id = check_if_exists_torunament.id
            else:
                new_league_or_tournament = LeagueOrTournament(
                    name=bet_data.league_or_tournament_str,
                    sport_id=bet_data.sport_id,
                    # location_id 1 is the default location
                    location_id=1
                )
                self.db.add(new_league_or_tournament)
                self.db.flush()
                bet_data.league_or_tournament_id = new_league_or_tournament.id

        new_individual_bet = IndividualBet(
            bet_status_id=bet_data.bet_status_id,
            event_date=bet_data.event_date,
            league_or_tournament_id=bet_data.league_or_tournament_id,
            odds=bet_data.odds,
            player_or_team1_id=bet_data.player_or_team1_id,
            player_or_team2_id=bet_data.player_or_team2_id,
            specific_bet=bet_data.specific_bet,
            sport_id=bet_data.sport_id,
            type_of_bet=bet_data.type_of_bet,
        )
        self.db.add(new_individual_bet)
        self.db.flush()  # Flush para obtener el ID
        return new_individual_bet
