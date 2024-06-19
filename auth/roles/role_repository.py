from typing import List, Optional

from sqlalchemy.orm import Session

from . import role_model, role_schemas


class RoleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_role(self, user_id: int) -> Optional[role_model.Role]:
        return self.db.query(role_model.Role).filter(role_model.Role.id == user_id).first()

    def get_roles(self, skip: int = 0, limit: int = 10) -> List[role_model.Role]:
        return self.db.query(role_model.Role).offset(skip).limit(limit).all()
    
    def create_role(self, role: role_schemas.RoleCreate) -> role_model.Role:
        db_role = role_model.Role(name=role.name)
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role
    
    def update_role(self, role: role_schemas.RoleCreate, role_id: int) -> role_model.Role:
        db_role = self.get_role(role_id)
        db_role.name = role.name
        self.db.commit()
        self.db.refresh(db_role)
        return db_role
    
    def delete_role(self, role_id: int) -> role_model.Role:
        db_role = self.get_role(role_id)
        self.db.delete(db_role)
        self.db.commit()
        return db_role