# Celery background tasks
from worker.tasks import app as celery_app

__all__ = ["celery_app"]