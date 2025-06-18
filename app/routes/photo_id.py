# app/routes/photo_id.py

from fastapi import APIRouter, UploadFile, File
from tasks.task_defs import async_generate_id_photo
import os

#接口地址为 POST /photo_id/generate

router = APIRouter(prefix="/photo_id", tags=["PhotoID"])

@router.post("/generate")
async def generate(file: UploadFile = File(...)):
    # 保存上传图片到 static/uploads/
    path = f"static/uploads/{file.filename}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())

    # 异步调用证件照生成任务
    task = async_generate_id_photo.delay(path)

    return {
        "status": "submitted",
        "task_id": task.id,
        "filename": file.filename
    }
