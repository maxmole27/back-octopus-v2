
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class PlayerOrTeam(Base):
    __tablename__ = 'player_or_teams'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    alternative_name = Column(String, nullable=True)
    alternative_name2 = Column(String, nullable=True)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship("Sport", back_populates="player_or_teams")

    individual_bets1 = relationship("IndividualBet", back_populates="player_or_teams1", foreign_keys='IndividualBet.player_or_teams1_id')
    individual_bets2 = relationship("IndividualBet", back_populates="player_or_teams2", foreign_keys='IndividualBet.player_or_teams2_id')
