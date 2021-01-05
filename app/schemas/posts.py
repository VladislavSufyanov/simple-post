from pydantic import BaseModel
from datetime import datetime


class BasePost(BaseModel):
    title: str
    text: str


class ResponsePost(BasePost):
    username: str
    date_pub: datetime


class CreatePost(BasePost):
    user_id: int


class PostInDB(CreatePost):
    id: int
    date_publication: datetime
