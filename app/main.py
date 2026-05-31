from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.logger import logger
from fastapi.responses import RedirectResponse
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('FastAPI Cache Initialized')
    yield
    logger.info('FastAPI Cache Initialized')
app = FastAPI(
    app_name=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)


@app.get('/', include_in_schema=False)
async def root():
    """
    Автоматическое перенаправление на страницу документации Swagger.
    """
    return RedirectResponse(url='/docs')