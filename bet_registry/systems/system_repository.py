from sqlalchemy.orm import joinedload

from ..betslips.betslip_model import Betslip
from ..betslips.betslip_repository import BetslipRepository
from ..betslips.betslip_schemas import BetslipResponse
from .system_model import System
from .system_schemas import SystemsCreate, SystemsGet, SystemsResponse


class SystemRepository:
  def __init__(self, db):
    self.db = db

  def get_system(self, system_id: int) -> System:
    return self.db.query(System).filter(System.id == system_id).first()
  
  def get_systems(self, page: int, limit: int)-> list[SystemsGet]:
    result = self.db.query(System).offset(page*limit).limit(limit).all()
    return result
  
  def create_system(self, system: SystemsCreate) -> SystemsGet:
    
    system_img_url = system.image_url if system.image_url else '/none.png'

    db_system = System(
      name=system.name, 
      description=system.description, 
      image_url= system_img_url, 
      is_backtesting=system.is_backtesting, 
      stake_by_default=system.stake_by_default, 
      bookie_by_default_id=system.bookie_by_default_id,
      initial_bankroll=system.initial_bankroll,
      sport_by_default_id=system.sport_by_default_id, 
      owner_id=system.owner_id)
    self.db.add(db_system)
    self.db.commit()
    self.db.refresh(db_system)
    return db_system
  
  def update_system(self, system_id: int, system: SystemsCreate) -> SystemsGet:
    db_system = self.get_system(system_id)
    db_system.name = system.name
    db_system.description = system.description
    db_system.image_url = system.image_url
    db_system.is_backtesting = system.is_backtesting
    db_system.initial_bankroll = system.initial_bankroll
    db_system.stake_by_default = system.stake_by_default
    db_system.bookie_by_default_id = system.bookie_by_default_id
    db_system.sport_by_default_id = system.sport_by_default_id
    db_system.owner_id = system.owner_id
    self.db.commit()
    self.db.refresh(db_system)
    return db_system
  
  def delete_system(self, system_id: int):
    db_system = self.get_system(system_id)
    self.db.delete(db_system)
    self.db.commit()
    return db_system 

  def count_systems(self) -> int:
    return self.db.query(System).count()
  
  # def get_systems_by_owner(self, owner_id: int, page: int, limit: int) -> list[SystemsGet]:
  #   result = self.db.query(System).filter(System.owner_id == owner_id).offset(page*limit).limit(limit).all()
  #   return result
  
 