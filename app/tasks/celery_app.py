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

# celery_instance.conf.beat_schedule = {
#     "send_email_for_security_user": {
#         "task": "send_email",
#         "schedule": crontab(hour="0", minute="0")
#     },
#     "name2": {
#         "task": "update_player_info",
#         "schedule": 230
#     },
#     "name3": {
#         "task": "update_fraction_info",
#         "schedule": 230
#     }
# }
