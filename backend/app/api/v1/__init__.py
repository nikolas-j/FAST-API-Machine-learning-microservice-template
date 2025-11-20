# API routing for v1

from fastapi import APIRouter
from app.api.v1 import data, predict

api_router = APIRouter()
api_router.include_router(data.router)
api_router.include_router(predict.router)