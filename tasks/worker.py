# tasks/worker.py
from tasks.celery_app import celery_app

if __name__ == "__main__":
    celery_app.worker_main()


#启动任务：  celery -A tasks.celery_app.celery_app worker --loglevel=info
#检查启动日志是否列出了 celery -A tasks.celery_app.celery_app inspect registered
