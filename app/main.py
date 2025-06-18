# app/main.py

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes import photo_id, cartoonize, paddleocr, task_status
from app.config import settings
from pathlib import Path
import uvicorn




app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="图像处理接口服务"
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.DEBUG else ["https://your.production.domain"],  # 生产环境换成具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_status.router) 
app.include_router(photo_id.router)
app.include_router(cartoonize.router)
app.include_router(paddleocr.router)

PROJECT_ROOT = Path(__file__).parent.resolve()

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    templates = Jinja2Templates(directory=PROJECT_ROOT / "templates")
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
 