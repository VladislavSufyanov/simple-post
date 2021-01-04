from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from crud.user import crud_user
from schemas.token import Token
from core.security import generate_token


router = APIRouter()


@router.post('/login/access-token', response_model=Token)
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await crud_user.authenticate(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bad username or password')
    access_token = generate_token(user.id)
    return {'access_token': access_token, 'token_type': 'bearer'}
