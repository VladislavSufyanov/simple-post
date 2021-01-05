from typing import List

from sqlalchemy.sql.dml import Insert
from sqlalchemy.sql import select
from sqlalchemy.sql.selectable import Select

from crud.base import CRUD
from db.db import db
from models.post import posts
from models.user import users
from schemas.posts import CreatePost, ResponsePost


class CRUDPosts(CRUD):
    async def get_user_posts(self, username: str) -> List[ResponsePost]:
        query: Select = select([self.table.c.date_pub, self.table.c.title, self.table.c.text]). \
            select_from(self.table.join(self.related_tables['users'])). \
            where(self.related_tables['users'].c.username == username). \
            order_by(self.table.c.date_pub.desc())
        rows = await db.fetch_all(query)
        return [ResponsePost(**row, username=username) for row in rows]

    async def create(self, username: str, post: CreatePost) -> ResponsePost:
        query: Insert = self.table.insert().returning(self.table.c.id, self.table.c.date_pub.label('date_pub'))
        returning_values = await db.fetch_one(query, post.dict())
        return ResponsePost(username=username, title=post.title, text=post.text,
                            date_pub=returning_values['date_pub'])


crud_post = CRUDPosts(posts, {'users': users})
