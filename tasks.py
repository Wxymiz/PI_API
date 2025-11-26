from celery import Celery
from decimal import Decimal, getcontext
import time

celery_app = Celery(
    "pi_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@celery_app.task(bind=True)
def calculate_pi(self, n):
    """
    Calculates PI using the Nilakantha series (improved Leibniz series), with Decimal precision.
    """

    # Setting precision of deciaml (larger than n to avoid errors)
    getcontext().prec = n + 5

    pi = Decimal(3)
    sign = 1

    total_iterations = n * 5

    for i in range(1, total_iterations):
        term = Decimal(4) / (Decimal(2*i) * Decimal(2*i + 1) * Decimal(2*i + 2))
        pi += Decimal(sign) * term
        sign *= -1

        # Update Celery data
        self.update_state(
            state="PROGRESS",
            meta={"progress": i / total_iterations}
        )

    return f"{pi:.{n}f}"
