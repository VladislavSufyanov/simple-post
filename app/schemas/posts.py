from pydantic import BaseModel
from datetime import datetime


class BasePost(BaseModel):
    title: str
    text: str


class PostID(BaseModel):
    id: int


class ResponsePost(BasePost, PostID):
    username: str
    date_pub: datetime


class CreatePost(BasePost):
    user_id: int


class PostInDB(CreatePost, PostID):
    date_pub: datetime
