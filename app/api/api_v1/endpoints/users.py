from fastapi import APIRouter

from schemas.user import ResponseUser, CreateUser
from crud.user import crud_user


router = APIRouter()


@router.post('/', response_model=ResponseUser)
async def create_user(new_user: CreateUser):
    return await crud_user.create(new_user)
