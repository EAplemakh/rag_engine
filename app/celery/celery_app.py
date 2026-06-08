from celery import Celery

from app.config import settings

celery_app = Celery("rag_engine", broker=settings.rabbitmq_url)
celery_app.conf.update(task_track_started=True)
