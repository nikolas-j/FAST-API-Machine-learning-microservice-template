# Initialize and run FastAPI app

from fastapi import FastAPI
from app.core.config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from backend.app.models import ml_model
from contextlib import asynccontextmanager

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    yield
    # Cleanup

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.v1 import api_router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"status": "Ok"}


