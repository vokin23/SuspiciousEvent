from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_instance = Celery(
    "tasks",
    broker=settings.redis_url,
    include=[
        "app.tasks.tasks"
    ]
)

celery_instance.conf.beat_schedule = {
    "name1": {
        "task": "name_function",
        "schedule": crontab(hour="0", minute="0")
    },
    "name2": {
        "task": "name_function",
        "schedule": 230
    },
    "name3": {
        "task": "name_function",
        "schedule": 230
    }
}
