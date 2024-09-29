from datetime import datetime
from typing import List

from pydantic import BaseModel

from ..individual_bets.individual_bet_schemas import IndividualBetCreate


class BetslipBase(BaseModel):
    system_id: int

class BetslipCreate(BetslipBase):
    individual_bets: List[IndividualBetCreate]

    class Config:
        orm_mode = True

class BetslipGet(BetslipBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # TODO: Add relationship with system
    # TODO: Add relationship with individual bets.

    class Config:
        from_attributes = True

class BetslipsResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[BetslipGet]
    message: str = None
    code: int = None

class BetslipsDelete(BaseModel):
    id: int