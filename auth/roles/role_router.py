from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .role_repository import RoleRepository
from .role_schemas import RoleCreate, RoleGet

router = APIRouter(
  prefix="/roles",
  tags=["roles"],
  responses={404: {"description": "Roles Not found"}}
)

@router.get("/", response_model=List[RoleGet])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    role_repo = RoleRepository(db)
    bookies = role_repo.get_roles(skip=skip, limit=limit)
    return bookies

@router.post("/", response_model=RoleGet)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    role_repo = RoleRepository(db)
    return role_repo.create_role(role)

@router.put("/{role_id}", response_model=RoleGet)
def update_role(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    role_repo = RoleRepository(db)
    return role_repo.update_role(role, role_id)

@router.delete("/{role_id}", response_model=RoleGet)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role_repo = RoleRepository(db)
    return role_repo.delete_role(role_id)