from loguru import logger
from app.exceptions.base import ObjectAlreadyExistException, PageAlreadyExistsException
from app.schemas.pages import PageCreate
from app.services.base import BaseService

class PagesService(BaseService):
    async def add_url(self, page: PageCreate):
        try:
            page = await self.db.pages.add(page.model_dump(mode="json"))
            await self.db.commit()
            logger.info(f"Page url created successfully",
                        updated_data=page.model_dump(exclude_unset=True, mode="json"))
        except ObjectAlreadyExistException:
            raise PageAlreadyExistsException
        return page