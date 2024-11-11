from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.type_adapter import TypeAdapter
from sqlalchemy.orm import Session

from ...database import get_db
from ...shared.utils.constants import CODE_NO_MORE_DATA, CODE_OK
from ..individual_bets.individual_bet_repository import IndividualBetRepository
from .betslip_repository import BetslipRepository
from .betslip_schemas import (BetslipCreate, BetslipGet, BetslipResponse,
                              BetslipUpdate)
from .betslip_service import BetslipService

router = APIRouter(
  prefix="/betslips",
  tags=["betslips"],
  responses={404: {"description": "Not found betslip/s"}},
)

@router.get("/{betslip_id}", response_model=BetslipGet)
def read_betslip(betslip_id: int, db = Depends(get_db)):
    betslip_repo = BetslipRepository(db)
    return betslip_repo.get_betslip(betslip_id)

# Probably this route will be removed. It is not necessary to get all the betslips without a system_id
@router.get("/", response_model=BetslipResponse)
def read_betslips(page: int = 0, limit: int = 10, start_date = None, end_date = None, team_name = None, db = Depends(get_db)):
    betslip_repo = BetslipRepository(db)
    betslips = betslip_repo.get_betslips(page=page, limit=limit)
    total = betslip_repo.count_betslips(1)
    totalPages = (total // limit) + 1
    if page+1 > totalPages:
        response = BetslipResponse(
            currentPage=page,
            totalPages=totalPages,
            totalItems=total,
            data=[],
            message="No more pages",
            code=CODE_NO_MORE_DATA
        )
        return response

    response = BetslipResponse(
        currentPage=page,
        totalPages=totalPages,
        totalItems=total,
        data=betslips,
        message="Betslips retrieved successfully",
        code=CODE_OK
    )

    return response

# @router.post("/", response_model=BetslipCreate)
# def create_betslip(betslip: BetslipCreate, db = Depends(get_db)):
#     betslip_repo = BetslipRepository(db)
#     return betslip_repo.create_betslip(betslip)

@router.post("/", response_model=BetslipCreate)
def create_betslip(betslip_data: BetslipCreate, db: Session = Depends(get_db)):
    # Inyectar repositorios y servicio
    betslip_repo = BetslipRepository(db)
    individual_bet_repo = IndividualBetRepository(db)
    betslip_service = BetslipService(db, betslip_repo, individual_bet_repo)
    
    # Llamar al servicio para crear la Betslip
    new_betslip = betslip_service.create_betslip_with_individual_bets(
        betslip_data=betslip_data, 
        individual_bets_data=betslip_data.individual_bets,
    )
    return new_betslip


@router.put("/{betslip_id}")
def update_betslip(betslip_id: int, betslip_data: BetslipUpdate, db = Depends(get_db)):
    betslip_repo = BetslipRepository(db)
    individual_bet_repo = IndividualBetRepository(db)
    betslip_service = BetslipService(db, betslip_repo, individual_bet_repo)

    new_betslip = betslip_service.update_betslip_with_individual_bets(betslip_id, betslip_data, betslip_data.individual_bets)

    return new_betslip

@router.delete("/{betslip_id}")
def delete_betslip(betslip_id: int, db = Depends(get_db)):
    betslip_repo = BetslipRepository(db)
    return betslip_repo.delete_betslip(betslip_id)

@router.get("/system/{system_id}", response_model=BetslipResponse)
def read_betslips_from_system(system_id: int, page: int = 0, limit: int = 10, start_date = None, end_date = None, team_name = None, db = Depends(get_db)):
    betslip_repo = BetslipRepository(db)
    betslip_repo_res = betslip_repo.get_betslips_from_system(system_id, page=page, limit=limit, start_date=start_date, end_date=end_date, team_name=team_name)
    betslips = betslip_repo_res[0]
    
    total = betslip_repo_res[1]
    totalPages = (total // limit) + 1 if total % limit > 0 else total // limit


    if page+1 > totalPages:
        response = BetslipResponse(
            currentPage=page,
            totalPages=totalPages,
            totalItems=total,
            data=[],
            message="No more pages",
            code=CODE_NO_MORE_DATA
        )
        return response

    response = BetslipResponse(
        currentPage=page,
        totalPages=totalPages,
        totalItems=total,
        data=betslips,
        message="Betslips retrieved successfully",
        code=CODE_OK
    )

    return response