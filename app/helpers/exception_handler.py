from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.base import BaseAppHTTPException


def add_exception_handler(app: FastAPI):
    @app.exception_handler(BaseAppHTTPException)
    async def base_app_exception_handler(request: Request, exc: BaseAppHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )