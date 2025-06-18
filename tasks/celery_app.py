# tasks/celery_app.py
from celery import Celery
from app.config import settings

celery_app = Celery(
    "tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["tasks.task_defs"]
)

celery_app.conf.task_track_started = True
celery_app.autodiscover_tasks(["tasks"])
