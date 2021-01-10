from urllib.parse import urljoin

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from core.config import settings
from core.security import decode_token
from crud.user import crud_user
from schemas.user import UserInDB


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=urljoin(settings.API_V1_STR if settings.API_V1_STR.endswith('/') else settings.API_V1_STR + '/',
                     'login/access-token')
)


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    token_data = decode_token(token)
    if token_data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials',
                            headers={'WWW-Authenticate': 'Bearer'})
    user = await crud_user.get_by_id(token_data.sub)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found',
                            headers={'WWW-Authenticate': 'Bearer'})
    return user
