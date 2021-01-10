from typing import List, Optional

from sqlalchemy.sql.dml import Insert, Delete
from sqlalchemy.sql import select
from sqlalchemy.sql.selectable import Select
from sqlalchemy.sql.operators import and_

from crud.base import CRUD
from db.db import db
from models.post import posts
from models.user import users
from schemas.posts import CreatePost, ResponsePost, PostID


class CRUDPosts(CRUD):
    async def get_user_posts(self, username: str) -> List[ResponsePost]:
        query: Select = select([self.table.c.id, self.table.c.date_pub,
                                self.table.c.title, self.table.c.text]). \
            select_from(self.table.join(self.related_tables['users'])). \
            where(self.related_tables['users'].c.username == username). \
            order_by(self.table.c.date_pub.desc())
        rows = await db.fetch_all(query)
        return [ResponsePost(**row, username=username) for row in rows]

    async def create(self, username: str, post: CreatePost) -> ResponsePost:
        query: Insert = self.table.insert().returning(self.table.c.id, self.table.c.date_pub.label('date_pub'))
        returning_values = await db.fetch_one(query, post.dict())
        return ResponsePost(username=username, title=post.title, text=post.text,
                            date_pub=returning_values['date_pub'], id=returning_values['id'])

    async def delete(self, post_id: int, current_user_id: int) -> Optional[PostID]:
        query: Delete = self.table.delete().\
            where(and_(self.table.c.id == post_id, self.table.c.user_id == current_user_id)).\
            returning(self.table.c.id)
        deleted_post_id = await db.execute(query)
        if deleted_post_id is None:
            return
        return PostID(id=deleted_post_id)


crud_post = CRUDPosts(posts, {'users': users})
