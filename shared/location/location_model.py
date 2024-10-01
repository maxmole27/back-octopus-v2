from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    flag = Column(String, nullable=False)
    code = Column(String, nullable=False)
    # Location can be a country, continent, city, etc. So if we need just countries we can filter by is_country
    is_country = Column(Boolean, nullable=False)

    league_or_tournament = relationship("LeagueOrTournament", back_populates="location")
