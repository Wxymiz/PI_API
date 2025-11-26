from fastapi import FastAPI
from celery.result import AsyncResult
from task import celery_app, calculate_pi

app = FastAPI(title="Async Pi Calculator API")


@app.get("/calculate_pi")
def start_calculation(n: int):
    """Starts async calculation and returns task ID."""
    task = calculate_pi.delay(n)
    return {"task_id": task.id}


@app.get("/check_progress")
def check_progress(task_id: str):
    """Returns current progress or final result of calculation."""
    task = AsyncResult(task_id, app=celery_app)

    if task.state == "PENDING":
        return {"state": "PROGRESS", "progress": 0, "result": None}

    if task.state == "PROGRESS":
        return {
            "state": "PROGRESS",
            "progress": task.info.get("progress"),
            "result": None
        }

    if task.state == "SUCCESS":
        return {"state": "FINISHED", "progress": 1.0, "result": task.get()}

    return {"state": task.state}
