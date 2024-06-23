from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from ...database import Base


class Bookie(Base):
  __tablename__ = 'bookies'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, unique=True, index=True)
  description = Column(String, nullable=True)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  class Config:
    from_attributes = True

   