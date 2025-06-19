# app/routes/ocr.py
from fastapi import APIRouter, UploadFile, File
from tasks.task_defs import async_recognize_text
import os

router = APIRouter(prefix="/paddleocr")

@router.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    path = f"static/uploads/{file.filename}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())
    task = async_recognize_text.delay(path)

    return {
        "status": "submitted",
        "task_id": task.id, 
    }
