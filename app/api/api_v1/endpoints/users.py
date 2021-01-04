from typing import Any

from fastapi import APIRouter, HTTPException, status, Depends

from schemas.user import ResponseUser, CreateUser, UserInDB
from crud.user import crud_user
from api.dependencies.users import get_current_user


router = APIRouter()


@router.get('/', response_model=ResponseUser)
async def get_user(username: str, current_user: UserInDB = Depends(get_current_user)):
    user = await crud_user.get_by_username(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user


@router.post('/', response_model=ResponseUser)
async def create_user(new_user: CreateUser) -> Any:
    resp_user = await crud_user.create(new_user)
    if resp_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad username or password')
    return resp_user
