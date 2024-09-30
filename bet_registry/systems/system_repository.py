from sqlalchemy.orm import joinedload

from ..betslips.betslip_model import Betslip
from ..betslips.betslip_repository import BetslipRepository
from ..betslips.betslip_schemas import BetslipsResponse
from .system_model import System
from .system_schemas import (SystemGetWithBetslips, SystemsCreate, SystemsGet,
                             SystemsResponse)


class SystemRepository:
  def __init__(self, db):
    self.db = db

  def get_system(self, system_id: int) -> System:
    return self.db.query(System).filter(System.id == system_id).first()
  
  def get_systems(self, page: int, limit: int)-> list[SystemsGet]:
    result = self.db.query(System).offset(page*limit).limit(limit).all()
    return result
  
  def create_system(self, system: SystemsCreate) -> SystemsGet:
    db_system = System(name=system.name, description=system.description, image_url=system.image_url, is_backtesting=system.is_backtesting, stake_by_default=system.stake_by_default, bookie_by_default=system.bookie_by_default, sport_by_default=system.sport_by_default, owner_id=system.owner_id)
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
    db_system.bookie_by_default = system.bookie_by_default
    db_system.sport_by_default = system.sport_by_default
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
  
  def get_system_with_betslips(self, system_id: int, page: int, limit: int) -> SystemGetWithBetslips:
      br = BetslipRepository(self.db)
      system = self.get_system(system_id)
      betslips = self.db.query(Betslip).filter(Betslip.system_id == system_id).offset(page*limit).limit(limit).all()
      total_betslips = br.count_betslips(system_id=system_id)
      return {
          "system": system,
          "betslips": BetslipsResponse(
            currentPage=page,
            totalPages=total_betslips // limit + 1,
            totalItems=total_betslips,
            data=betslips,
            message="Betslips retrieved successfully",
            code=200)
      }