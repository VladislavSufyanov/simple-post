from urllib.parse import urljoin

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from core.config import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=urljoin(settings.API_V1_STR if settings.API_V1_STR.endswith('/') else settings.API_V1_STR + '/',
                     'login/access-token')
)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    ...
