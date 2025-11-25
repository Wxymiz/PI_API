from celery import Celery

celery_app = Celery(
    "pi_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@celery_app.task(bind=True)
def calculate_pi(self, n):

    return "Something"
