# app/routes/task_status.py

from fastapi import APIRouter, HTTPException
from celery.result import AsyncResult
from app.config import settings
from tasks.worker import celery_app

router = APIRouter(prefix="/task", tags=["Task"])

@router.get("/{task_id}")
async def get_task_status(task_id: str):
    task = AsyncResult(task_id, app=celery_app)
    state = task.state  # PENDING, STARTED, SUCCESS, FAILURE

    ret = {
        "task_id": task_id,
        "status": state,
        "error": "",
        "result": ""
    }

    print(task.result)
    if state == "SUCCESS":
        result = task.result
        if isinstance(result, dict) and result.get("status") == "SUCCESS":
            ret["status"] = "SUCCESS"
            ret["result"] = result.get("result")
        else:
            ret["status"] = "ERROR"
            ret["error"] = result.get("error", "Unknown error") if isinstance(result, dict) else str(result)

    elif state == "FAILURE":
        # 捕获异常信息
        try:
            ret["error"] = str(task.result)
        except Exception as e:
            ret["error"] = f"Failed to get error: {e}"
        ret["status"] = "ERROR"

    return ret