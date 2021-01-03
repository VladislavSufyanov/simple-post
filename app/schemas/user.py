from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str = Field(..., example='user', min_length=1, max_length=50)


class CreateUser(BaseUser):
    plain_password: str = Field(..., example='32ptyS69Ise3mquNTavs', min_length=5, max_length=50)


class User(BaseUser):
    password: str


class ResponseUser(BaseUser):
    id: int
