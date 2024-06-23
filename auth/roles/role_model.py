from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Role(Base):
  __tablename__ = 'roles'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, unique=True, index=True)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  users = relationship("User", back_populates="role")


    