from asyncpg.exceptions import UniqueViolationError
from fastapi import HTTPException, status

from models.user import users
from crud.base import CRUD
from schemas.user import CreateUser, User, ResponseUser
from core.security import get_password_hash
from db.db import db


class CRUDUser(CRUD):
    async def create(self, obj_user: CreateUser) -> ResponseUser:
        db_user = User(username=obj_user.username,
                       password=get_password_hash(obj_user.plain_password))
        query = self.table.insert().values(**db_user.dict())
        try:
            user_id = await db.execute(query)
        except UniqueViolationError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad username or password')
        return ResponseUser(id=user_id, username=obj_user.username)


crud_user = CRUDUser(users)
