from app.mappers.base import DataMapper
from app.models.page_logs import PageLogsORM
from app.schemas.page_logs import PageLogResponse

class PageLogsMapper(DataMapper):
    db_model = PageLogsORM
    schema = PageLogResponse