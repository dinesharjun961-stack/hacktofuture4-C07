

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "redblueai",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.tasks.red_tasks", "app.tasks.blue_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
)
