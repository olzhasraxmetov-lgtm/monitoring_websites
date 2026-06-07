import asyncio
import time

from app.tasks.celery_app import celery_app
from app.core.database import get_async_session_null_pool
from app.repositories.pages import PagesRepository
from app.repositories.page_logs import PageLogsORM
from loguru import logger
import httpx

async def check_one_url(client: httpx.AsyncClient, page, session):
    start_time = time.monotonic()
    url_str = page.url.unicode_string() if hasattr(page.url, 'unicode_string') else str(page.url)
    try:
        response = await client.get(url_str, timeout=10.0)
        response_time = time.monotonic() - start_time
        status_code = response.status_code
    except httpx.RequestError as exc:
        response_time = time.monotonic() - start_time
        status_code = None
        logger.warning(f"Ошибка при запросе к {url_str}: {exc}")

    log_entry = PageLogsORM(
        page_id=page.id,
        status_code=status_code,
        response_time=response_time
    )
    session.add(log_entry)

@celery_app.task(name="monitoring_websites")
def monitoring_websites():
    async def _logic():
        async with get_async_session_null_pool() as session:
            repo = PagesRepository(session)
            all_pages = await repo.get_all()

            if not all_pages:
                logger.info("No urls in database")
                return

            async with httpx.AsyncClient() as client:
                tasks = [check_one_url(client, page, session) for page in all_pages]

                await asyncio.gather(*tasks)

            await session.commit()
            logger.info(f"Успешно проверено сайтов: {len(all_pages)}")

    return asyncio.run(_logic())
