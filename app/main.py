from fastapi import FastAPI

from api.api_v1.api import api_router
from core.config import settings
from db.db import db


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()
