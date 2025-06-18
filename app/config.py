# app/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # FastAPI 基础配置
    APP_NAME: str = "图像处理服务"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Celery 配置
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

    # 百度翻译API配置
    BAIDU_APP_ID: str = os.getenv("BAIDU_APP_ID", "")
    BAIDU_APP_KEY: str = os.getenv("BAIDU_APP_KEY", "")

    # 上传文件夹
    UPLOAD_DIR: str = "static/uploads"
    OUTPUT_DIR: str = "static/outputs"

    # 其它配置项
    ALLOWED_IMAGE_EXTENSIONS: set[str] = {"jpg", "jpeg", "png"} # 添加 Set[str] 类型注解

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
