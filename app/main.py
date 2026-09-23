import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title="AI Learning Lab",
    description="我的 AI 应用开发学习实验",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {
        "message": "Hello, AI Learning Lab!",
        "environment": os.getenv("APP_ENV", "development"),
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}