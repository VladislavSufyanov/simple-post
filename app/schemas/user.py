from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class CreateUser(BaseUser):
    plain_password: str


class User(BaseUser):
    password: str


class ResponseUser(BaseUser):
    id: int
