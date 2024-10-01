from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, Double, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from ...database import Base


class System(Base):
  __tablename__ = 'systems'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String)
  description = Column(String)
  image_url = Column(String)
  initial_bankroll = Column(Double)
  is_backtesting = Column(Boolean)
  stake_by_default = Column(Double)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  bookie_by_default_id = Column(Integer, ForeignKey('bookies.id'))
  sport_by_default_id = Column(Integer, ForeignKey('sports.id'))
  owner_id = Column(Integer, ForeignKey('users.id'))
  bookie_by_default = relationship("Bookie", back_populates="systems")
  sport_by_default = relationship("Sport", back_populates="systems")
  owner = relationship("User", back_populates="systems")

  betslips = relationship("Betslip", back_populates="system")