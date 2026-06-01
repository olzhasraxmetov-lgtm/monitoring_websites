from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.logger import logger
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.helpers.exception_handler import add_exception_handler
from app.api.v1.pages import router as pages_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('FastAPI Initialized')
    yield
    logger.info('FastAPI Finished')
app = FastAPI(
    app_name=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(pages_router)
add_exception_handler(app=app)
@app.get('/', include_in_schema=False)
async def root():
    """
    Автоматическое перенаправление на страницу документации Swagger.
    """
    return RedirectResponse(url='/docs')