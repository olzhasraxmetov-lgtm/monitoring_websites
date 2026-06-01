from fastapi import APIRouter
from app.schemas.pages import PageCreate
from app.services.pages import PagesService
from app.core.dependencies import DBDep
router = APIRouter(
    prefix="/pages",
    tags=["Сайты"]
)

@router.post("", summary="Добавить новый сайт")
async def add_website_url(db: DBDep, payload: PageCreate):
    return await PagesService(db).add_url(payload)