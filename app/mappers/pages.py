from app.mappers.base import DataMapper
from app.models.pages import PagesORM
from app.schemas.pages import PageResponse

class PagesMapper(DataMapper):
    db_model = PagesORM
    schema = PageResponse