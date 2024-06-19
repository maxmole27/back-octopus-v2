from sqlalchemy import Column, Integer, String

from ...database import Base


class Bookie(Base):
  __tablename__ = 'bookies'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, unique=True, index=True)
  description = Column(String, nullable=True) 

  class Config:
    orm_mode = True

   