from typing import Optional

from ...shared.utils.hash_password import check_password, hash_password
from .user_model import User
from .user_schemas import UserCreate, UserGet


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_users(self, skip: int = 0, limit: int = 10)-> list[UserGet]:
        result = self.db.query(User).offset(skip).limit(limit).all()
        return result
    
    def create_user(self, user: UserCreate) -> User:
        db_user = User(name=user.name, email=user.email, password=hash_password(user.password), role_id=user.role_id, username=user.username)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, user_id: int) -> User:
        user = self.get_user(user_id)
        self.db.delete(user)
        self.db.commit()
        return user
    
    def count_users(self):
        return self.db.query(User).count()
    
    def do_login(self, username: str, password: str) -> Optional[User]:
        find_user_by_username: User = self.db.query(User).filter(User.username == username)
        if not find_user_by_username.first():
            return None
        usrname = find_user_by_username.first()
        print('woooooop')
        print(usrname.name)
        if check_password(hashed_password=usrname.password, password=password):
            return usrname
        return None