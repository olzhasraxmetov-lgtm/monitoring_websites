from fastapi import APIRouter
from app.schemas.pages import PageCreate
from app.services.pages import PagesService
from app.core.dependencies import DBDep
from app.schemas.pages import PageDetail
router = APIRouter(
    prefix="/pages",
    tags=["Сайты"]
)

@router.post("", summary="Добавить новый сайт")
async def add_website_url(db: DBDep, payload: PageCreate):
    return await PagesService(db).add_url(payload)

@router.get("/{page_id}/stats", summary="Получить информацию о сайте", response_model=PageDetail)
async def get_websites_info(db: DBDep, page_id: int):
    return await PagesService(db).get_page_info(page_id=page_id)