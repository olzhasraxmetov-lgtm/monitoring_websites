from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.exceptions.base import ObjectNotFoundException
from app.repositories.base import BaseRepository
from app.models.pages import PagesORM
from app.mappers.pages import PagesMapper

class PagesRepository(BaseRepository):
    model = PagesORM
    mapper = PagesMapper

    async def get_page_log(self, page_id: int):
        query = (
            select(self.model)
            .where(self.model.id == page_id)
            .options(
                selectinload(self.model.logs)
            )
        )
        result = await self.session.execute(query)
        log = result.unique().scalar_one_or_none()
        if not log:
            raise ObjectNotFoundException
        return log