
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ...database import Base
from ..individual_bets.individual_bet_model import IndividualBetBetslip


class Betslip(Base):
    __tablename__ = 'betslips'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    system_id = Column(Integer, ForeignKey('systems.id'))
    system = relationship("System", back_populates="betslips")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    bookie_id = Column(Integer, ForeignKey('bookies.id'))
    bookie = relationship("Bookie", back_populates="betslips")
    stake = Column(Integer)
    money_stake = Column(Integer)

    individual_bets = relationship("IndividualBet", secondary='individual_bet_betslip' ,back_populates="betslip")
