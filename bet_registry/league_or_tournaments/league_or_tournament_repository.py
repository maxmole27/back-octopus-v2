from .league_or_tournament_model import LeagueOrTournament
from .league_or_tournament_schema import (LeagueOrTournamentCreate,
                                          LeagueOrTournamentGet)


class LeagueOrTournamentRepository:
    def __init__(self, db):
        self.db = db

    def get_league_or_tournament(self, league_or_tournament_id: str) -> LeagueOrTournamentGet:
        return self.db.query(LeagueOrTournament).filter(
            LeagueOrTournament.id == league_or_tournament_id).first()
    
    def get_league_or_tournaments_by_sport_raw(self, sport_id: int) -> list[LeagueOrTournamentGet]:
        return self.db.query(LeagueOrTournament).filter(
            LeagueOrTournament.sport_id == sport_id).all()
        
  
    def create_league_or_tournament(self, league_or_tournament: LeagueOrTournamentCreate) -> LeagueOrTournamentGet:
        db_league_or_tournament = LeagueOrTournament(
            name=league_or_tournament.name,
            description=league_or_tournament.description,
            image_url=league_or_tournament.image_url,
            sport_id=league_or_tournament.sport_id,
            location_id=league_or_tournament.location_id,
            alternative_name=league_or_tournament.alternative_name,
            alternative_name2=league_or_tournament.alternative_name2
        )
        self.db.add(db_league_or_tournament)
        self.db.commit()
        self.db.refresh(db_league_or_tournament)
        return db_league_or_tournament
    
