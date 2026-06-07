from typing import Any
from fastapi import HTTPException, status


class BaseAppHTTPException(HTTPException):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "Внутренняя ошибка сервера"
    log_level: str = "ERROR"

    def __init__(self, detail: str | None = None, log_message: str | None = None, **kwargs: Any):
        current_detail = detail or self.detail

        super().__init__(status_code=self.status_code, detail=current_detail)

        self.log_message = log_message or current_detail
        self.extra = kwargs

class ObjectAlreadyExistException(BaseAppHTTPException):
    detail = "Похожий объект уже существует"
    status_code = 409

class ObjectNotFoundException(BaseAppHTTPException):
    detail = "Объект не найден"
    status_code = 404

class PageAlreadyExistsException(BaseAppHTTPException):
    status_code = 409
    detail = "Этот URL уже добавлен в систему мониторинга"
    log_level = "INFO"

class PageNotFoundException(ObjectNotFoundException):
    detail = "Сайт не найден"