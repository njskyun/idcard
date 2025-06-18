# app/routes/cartoonize.py

from fastapi import APIRouter, UploadFile, File
from tasks.task_defs import async_cartoonize_gan
import os

router = APIRouter(prefix="/cartoonize", tags=["Cartoonize"])

@router.post("/generate")
async def generate(file: UploadFile = File(...)):
    # 保存上传文件到 static/uploads/
    path = f"static/uploads/{file.filename}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())
    
    # 异步调用卡通化任务
    task = async_cartoonize_gan.delay(path)

    return {
        "status": "submitted",
        "task_id": task.id,
        "filename": file.filename
    }
