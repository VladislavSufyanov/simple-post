from typing import Union, Any, Optional
from datetime import timedelta, datetime

from passlib.context import CryptContext
from jose import jwt
from pydantic import ValidationError

from core.config import settings
from schemas.token import TokenPayload


ALGORITHM = 'HS256'

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def generate_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {'sub': str(subject), 'exp': expire}
    jwt_token = jwt.encode(token_data, settings.SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


def decode_token(token: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        return
    return token_data


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def get_password_hash(plain_password: str) -> str:
    return pwd_context.hash(plain_password)
