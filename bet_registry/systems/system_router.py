from fastapi import APIRouter, Depends

from ...database import get_db
from ...shared.utils.constants import CODE_NO_MORE_DATA, CODE_OK
from ..betslips.betslip_schemas import BetslipResponse
from .system_repository import SystemRepository
from .system_schemas import SystemsCreate, SystemsGet, SystemsResponse

router = APIRouter(
    prefix="/systems",
    tags=["systems"],
    responses={404: {"description": "Not found system/s"}},
)

@router.get("/{system_id}", response_model=SystemsGet)
def read_system(system_id: int, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    return system_repo.get_system(system_id)

@router.get("/", response_model=SystemsResponse)
def read_systems(page: int = 0, limit: int = 10, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    systems = system_repo.get_systems(page=page, limit=limit)
    total = system_repo.count_systems()
    totalPages = (total // limit) + 1 if total % limit > 0 else total // limit
    if page+1 > totalPages:
        response = SystemsResponse(
            currentPage=page,
            totalPages=totalPages,
            totalItems=total,
            data=[],
            message="No more pages",
            code=CODE_NO_MORE_DATA
        )
        return response

    response = SystemsResponse(
        currentPage=page,
        totalPages=totalPages,
        totalItems=total,
        data=systems,
        message="Systems retrieved successfully",
        code=CODE_OK
    )

    return response

@router.post("/", response_model=SystemsCreate)
def create_system(system: SystemsCreate, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    return system_repo.create_system(system)

@router.put("/{system_id}", response_model=SystemsCreate)
def update_system(system_id: int, system: SystemsCreate, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    return system_repo.update_system(system_id, system)

@router.delete("/{system_id}")
def delete_system(system_id: int, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    res = system_repo.delete_system(system_id)
    return res 

@router.get("/{system_id}/bets", response_model=BetslipResponse)
def read_system_with_betslips(system_id: int, page: int = 0, limit: int = 10, db = Depends(get_db)):
    system_repo = SystemRepository(db)
    return system_repo.get_system_with_betslips(system_id, page, limit)