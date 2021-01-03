from fastapi import APIRouter, HTTPException, status

from schemas.user import ResponseUser, CreateUser
from crud.user import crud_user


router = APIRouter()


@router.post('/', response_model=ResponseUser)
async def create_user(new_user: CreateUser):
    resp_user = await crud_user.create(new_user)
    if resp_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad username or password')
    return resp_user
