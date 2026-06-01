from app.repositories.base import BaseRepository
from app.models.pages import PagesORM
from app.mappers.pages import PagesMapper

class PagesRepository(BaseRepository):
    model = PagesORM
    mapper = PagesMapper