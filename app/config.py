# app/config.py
import os
from pydantic_settings import BaseSettings
import redis
import json

class Settings(BaseSettings):
    # FastAPI 基础配置
    APP_NAME: str = "图像处理服务"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Celery 配置
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

    # OPENAI配置
    ZhipuAI_API_KEY: str = os.getenv("ZhipuAI_API_KEY", "") 
    LLM_SESSION: str = os.getenv("LLM_SESSION", "session") 
    MODEL_NAME: str = os.getenv("MODEL_NAME", "glm-4-flash")
    # 上传文件夹
    UPLOAD_DIR: str = "static/uploads"
    OUTPUT_DIR: str = "static/outputs"
 
    # Redis 客户端 
    def get_redis_client(self):
        return redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True
    ) 


    # 其它配置项
    ALLOWED_IMAGE_EXTENSIONS: set[str] = {"jpg", "jpeg", "png"} # 添加 Set[str] 类型注解


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
