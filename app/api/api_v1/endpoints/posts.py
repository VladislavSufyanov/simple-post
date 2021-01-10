from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies.users import get_current_user
from schemas.user import UserInDB
from schemas.posts import ResponsePost, BasePost, CreatePost, PostID
from crud.posts import crud_post


router = APIRouter()


@router.get('/{username}', response_model=List[ResponsePost])
async def get_user_posts(username: str, current_user: UserInDB = Depends(get_current_user)):
    user_posts = await crud_post.get_user_posts(username)
    return user_posts


@router.post('/', response_model=ResponsePost)
async def create_post(post: BasePost, current_user: UserInDB = Depends(get_current_user)):
    response_post = await crud_post.create(current_user.username, CreatePost(**post.dict(), user_id=current_user.id))
    return response_post


@router.delete('/{post_id}', response_model=PostID)
async def delete_post(post_id: int, current_user: UserInDB = Depends(get_current_user)):
    response_post = await crud_post.delete(post_id, current_user.id)
    if response_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    return response_post
