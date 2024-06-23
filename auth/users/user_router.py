from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .user_repository import UserRepository
from .user_schemas import UserCreate, UserGet, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found user/s"}},
)

@router.get("/", response_model=UserResponse)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    users = user_repo.get_users(skip=skip, limit=limit)
    total = user_repo.count_users()  # Necesitas implementar este método en tu repositorio
    
    response = UserResponse(
        currentPage=(skip // limit) + 1,
        totalPages=(total // limit) + 1 if total % limit > 0 else total // limit,
        totalItems=total,
        data=users,
        message="Users retrieved successfully",
        code=0
    )
    return response

@router.get("/a", response_model=list[UserGet])
def read_users_a(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.get_users(skip=skip, limit=limit)

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.create_user(user)