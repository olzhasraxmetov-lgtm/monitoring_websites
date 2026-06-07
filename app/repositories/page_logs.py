from app.repositories.base import BaseRepository
from app.models.page_logs import PageLogsORM
from app.mappers.page_logs import PageLogsMapper

class PageLogsRepository(BaseRepository):
    model = PageLogsORM
    mapper = PageLogsMapper

    async def get_all_urls(self):
        return await self.get_all()