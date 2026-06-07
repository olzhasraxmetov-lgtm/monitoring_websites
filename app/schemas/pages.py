from datetime import datetime
from pydantic import HttpUrl, computed_field

from pydantic import BaseModel, Field

class PageBase(BaseModel):
    url: HttpUrl

class PageCreate(PageBase):
     pass

class PageResponse(PageBase):
    id: int
    created_at: datetime

class LogInfo(BaseModel):
    id: int
    status_code: int | None
    response_time: float | None
    checked_at: datetime

class PageDetail(BaseModel):
    id: int
    url: HttpUrl
    logs: list[LogInfo]

    @computed_field
    def uptime_24h(self) -> float:
        if not self.logs:
            return 0.0

        total_checks = len(self.logs)
        # Считаем, сколько раз статус был 200
        success_checks = sum(1 for log in self.logs if log.status_code == 200)

        return round((success_checks / total_checks) * 100, 2)