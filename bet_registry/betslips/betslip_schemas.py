from datetime import datetime
from typing import List

from pydantic import BaseModel

from ..individual_bets.individual_bet_schemas import (IndividualBetCreate,
                                                      IndividualBetGet)


class BetslipBase(BaseModel):
    system_id: int

class BetslipCreate(BetslipBase):
    individual_bets: List[IndividualBetCreate]

    class Config:
        from_attributes = True

class BetslipGet(BetslipBase):
    id: int
    created_at: datetime
    updated_at: datetime
    individual_bets: List[IndividualBetGet]

    class Config:
        from_attributes = True

class BetslipResponse(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    data: List[BetslipGet]
    message: str = None
    code: int = None

class BetslipsDelete(BaseModel):
    id: int