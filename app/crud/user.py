from typing import Optional
from sqlalchemy.sql.dml import Insert
from sqlalchemy.sql.selectable import Select

from asyncpg.exceptions import UniqueViolationError

from models.user import users
from crud.base import CRUD
from schemas.user import CreateUser, User, ResponseUser, UserInDB
from core.security import get_password_hash, verify_password
from db.db import db


class CRUDUser(CRUD):
    async def create(self, obj_user: CreateUser) -> Optional[ResponseUser]:
        db_user = User(username=obj_user.username,
                       password=get_password_hash(obj_user.plain_password))
        query: Insert = self.table.insert().values(**db_user.dict())
        try:
            user_id = await db.execute(query)
        except UniqueViolationError:
            return
        return ResponseUser(id=user_id, username=obj_user.username)

    @staticmethod
    async def _fetch_one(query: Select) -> Optional[UserInDB]:
        raw = await db.fetch_one(query)
        if raw is None:
            return
        user = UserInDB(**raw)
        return user

    async def get_by_username(self, username: str) -> Optional[UserInDB]:
        query: Select = self.table.select().where(self.table.c.username == username)
        return await self._fetch_one(query)

    async def get_by_id(self, id_: int) -> Optional[UserInDB]:
        query: Select = self.table.select().where(self.table.c.id == id_)
        return await self._fetch_one(query)

    async def authenticate(self, username: str, password: str) -> Optional[UserInDB]:
        user = await self.get_by_username(username)
        if user is None:
            return
        if not verify_password(password, user.password):
            return
        return user


crud_user = CRUDUser(users)
