from fastapi import FastAPI , APIRouter
import os
router = APIRouter(
    prefix="/api/v1",
    tags=["/api/v1"]
)

@router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "message": f"Welcome to {app_name}!",
        "version": app_version
    }