# app/routes/task_status.py

from fastapi import APIRouter, HTTPException
from celery.result import AsyncResult
from app.config import settings
from tasks.worker import celery_app

router = APIRouter(prefix="/task", tags=["Task"])

@router.get("/{task_id}")
async def get_task_status(task_id: str):
    task = AsyncResult(task_id, app=celery_app)
    state = task.state  # e.g. PENDING, STARTED, SUCCESS, FAILURE

    if state == "PENDING":
        # 任务尚未入队或正在排队
        return {"task_id": task_id, "status": "PENDING"}
    elif state == "STARTED":
        return {"task_id": task_id, "status": "STARTED"}
    elif state == "SUCCESS":
        return {"task_id": task_id, "status": "SUCCESS", "result": task.result}
    elif state == "FAILURE":
        return {"task_id": task_id, "status": "FAILURE", "result": str(task.result)}
    else:
        return {"task_id": task_id, "status": state, "result": task.result}
