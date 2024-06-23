from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class User(Base):

  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  # role id 
  role_id = Column(Integer, ForeignKey('roles.id'))
  role = relationship("Role", back_populates="users")

