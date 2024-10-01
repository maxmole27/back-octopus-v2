from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class LeagueOrTournament(Base):
    __tablename__ = 'league_or_tournaments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship("Sport", back_populates="league_or_tournament")
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship("Location", back_populates="league_or_tournament")
    image_url = Column(String, nullable=True)
    alternative_name = Column(String, nullable=True)
    alternative_name2 = Column(String, nullable=True)
    description = Column(String, nullable=True)

    individual_bets = relationship("IndividualBet", back_populates="league_or_tournament")

