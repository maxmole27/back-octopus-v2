from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Sport(Base):
  __tablename__ = 'sports'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, unique=True, index=True)
  description = Column(String, nullable=True)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  systems = relationship("System", back_populates="sport")

  class Config:
    from_attributes = True

   