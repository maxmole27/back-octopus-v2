from datetime import datetime
from typing import List

from pydantic import BaseModel

from ..individual_bets.individual_bet_schemas import (IndividualBetCreate,
                                                      IndividualBetGet,
                                                      IndividualBetResponse,
                                                      IndividualBetUpdate)


class BetslipBase(BaseModel):
    system_id: int

class BetslipCreate(BetslipBase):
    individual_bets: List[IndividualBetResponse]
    bookie_id: int
    stake: float
    money_stake: float
    class Config:
        from_attributes = True

class BetslipUpdate(BaseModel):
    system_id: int
    individual_bets: List[IndividualBetUpdate]
    bookie_id: int
    stake: float
    money_stake: float
    class Config:
        from_attributes = True

class BetslipUpdateCompleted(BetslipUpdate):
    betslip_id: int
class BetslipGet(BetslipBase):
    id: int
    bookie_id: int
    stake: float
    money_stake: float
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