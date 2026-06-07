from celery import Celery
from app.core.config import settings

celery_app = (Celery
              ('tasks',
                broker=settings.REDIS_URL,
                backend=settings.REDIS_URL,
                include=["app.tasks"]
))

celery_app.autodiscover_tasks(['app.tasks'])

celery_app.conf.update(
    task_ignore_result=False,
    result_persistent=True,
)