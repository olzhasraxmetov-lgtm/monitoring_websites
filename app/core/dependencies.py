from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.database import AsyncSessionLocal
from app.utils.db_manager import DBManager

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_db():
    async with DBManager(session_factory=AsyncSessionLocal) as db:
        yield db

DBDep = Annotated[DBManager, Depends(get_db)]