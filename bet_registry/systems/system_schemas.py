from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ...auth.users.user_schemas import UserGet
from ...shared.bookies.bookie_schemas import BookieGet
from ...shared.sports.sport_schemas import SportGet
from ..betslips.betslip_schemas import BetslipsResponse


class SystemsBase(BaseModel):
    name: str
    description: str
    image_url: Optional[str]
    is_backtesting: bool
    initial_bankroll: Optional[float]
    stake_by_default: Optional[float]
    bookie_by_default: int
    sport_by_default: int
    owner_id: int


class SystemsCreate(SystemsBase):
    pass

class SystemsGet(SystemsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    owner: UserGet
    bookie: BookieGet
    sport: SportGet

    class Config:
        from_attributes = True

class SystemsResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[SystemsGet]
    message: str = None
    code: int = None

class SystemDelete(BaseModel):
    id: int

class SystemGetWithBetslips(BaseModel):
    betslips: BetslipsResponse
    system: SystemsGet
    class Config:
        from_attributes = True  