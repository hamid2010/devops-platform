from fastapi import FastAPI
from datetime import datetime, UTC
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "message": "DevOps Platform is running",
        "timestamp": datetime.now(UTC),
        "hostname": "..."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "application": "devops-platform",
        "version": "1.0.0",
        "environment": "development"
    }