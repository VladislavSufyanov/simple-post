from typing import Optional

from asyncpg.exceptions import UniqueViolationError

from models.user import users
from crud.base import CRUD
from schemas.user import CreateUser, User, ResponseUser
from core.security import get_password_hash
from db.db import db


class CRUDUser(CRUD):
    async def create(self, obj_user: CreateUser) -> Optional[ResponseUser]:
        db_user = User(username=obj_user.username,
                       password=get_password_hash(obj_user.plain_password))
        query = self.table.insert().values(**db_user.dict())
        try:
            user_id = await db.execute(query)
        except UniqueViolationError:
            return
        return ResponseUser(id=user_id, username=obj_user.username)


crud_user = CRUDUser(users)
