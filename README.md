# PI_API
An asynchronous π calculator built on FastAPI and Celery.

## About Project

This project calculates digits of PI asynchronously using:
- FastAPI (REST API)
- Celery (task queue)
- Redis (message broker and backend)

## Endpoints

- `/calculate_pi` - 1 param that specifies the number of decimals (e.g. `/calculate_pi?n=123`)
- `/check_progress` - 1 param that is id of task (e.g. `/check_progress?task_id=9f3d1b6a-1827-4c4b-8a2d-33de7b9e1f55`)

## Run with Docker:

```sh
docker-compose up --build
