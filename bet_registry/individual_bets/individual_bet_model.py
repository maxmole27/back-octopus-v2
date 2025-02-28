from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


# TABLA INTERMEDIA ENTRE INDIVIDUAL BET Y BETSLIP
class IndividualBetBetslip(Base):
    __tablename__ = 'individual_bet_betslip'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    individual_bet_id = Column(Integer, ForeignKey('individual_bets.id'))
    betslip_id = Column(Integer, ForeignKey('betslips.id'))




class IndividualBet(Base):
    __tablename__ = 'individual_bets'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    betslip = relationship("Betslip", secondary='individual_bet_betslip' ,back_populates="individual_bets")

    player_or_team1_id = Column(Integer, ForeignKey('player_or_teams.id'), nullable=True)
    player_or_team1 = relationship("PlayerOrTeam", back_populates="individual_bets1", foreign_keys=[player_or_team1_id])
    player_or_team2_id = Column(Integer, ForeignKey('player_or_teams.id'), nullable=True)
    player_or_team2 = relationship("PlayerOrTeam", back_populates="individual_bets2", foreign_keys=[player_or_team2_id])

    type_of_bet = Column(String, nullable=False)
    specific_bet = Column(String, nullable=False)

    event_date = Column(DateTime, nullable=True)

    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship("Sport", back_populates="individual_bets")

    bet_status_id = Column(Integer, ForeignKey('bet_status.id'))
    bet_status = relationship("BetStatus", back_populates="individual_bets")

    league_or_tournament_id = Column(Integer, ForeignKey('league_or_tournaments.id'))
    league_or_tournament = relationship("LeagueOrTournament", back_populates="individual_bets")

    odds = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
