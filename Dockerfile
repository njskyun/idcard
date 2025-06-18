version: '3.8'
services:
  redis:
    image: redis:latest
    ports:
      - "6379:6379"

  web:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
      - ./models:/app/models
      - ./static:/app/static
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/1
      - BAIDU_APP_ID=${BAIDU_APP_ID}
      - BAIDU_APP_KEY=${BAIDU_APP_KEY}
    ports:
      - "8000:8000"
    depends_on:
      - redis
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000

  worker:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
      - ./models:/app/models
      - ./static:/app/static
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/1
    depends_on:
      - redis
    command: celery -A tasks.worker.celery_app worker --loglevel=info
