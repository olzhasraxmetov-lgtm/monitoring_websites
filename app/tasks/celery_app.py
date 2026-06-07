from celery import Celery
from app.core.config import settings

celery_app = (Celery
              ('tasks',
                broker=settings.REDIS_URL,
                backend=settings.REDIS_URL,
                include=["app.tasks.monitoring_websites"]
))

celery_app.autodiscover_tasks(['app.tasks'])

celery_app.conf.update(
    task_ignore_result=False,
    result_persistent=True,
)

celery_app.conf.beat_schedule = {
    "get_urls_every_5_minutes": {
        "task": "monitoring_websites",
        "schedule": 180.0,
    },
}