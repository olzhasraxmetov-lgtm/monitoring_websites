from datetime import datetime
from pydantic import HttpUrl

from pydantic import BaseModel, Field

class PageBase(BaseModel):
    url: HttpUrl

class PageCreate(PageBase):
     pass

class PageResponse(PageBase):
    id: int
    created_at: datetime