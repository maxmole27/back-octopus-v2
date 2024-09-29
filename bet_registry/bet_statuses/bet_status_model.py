from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class BetStatus(Base):
    __tablename__ = 'bet_status'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    individual_bets = relationship("IndividualBet", back_populates="bet_status")