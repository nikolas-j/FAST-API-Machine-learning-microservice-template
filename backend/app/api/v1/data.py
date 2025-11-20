# GET endpoint for retrieving data

from fastapi import APIRouter, HTTPException
from app.services.external_api import fetch_external_data
from app.models.schemas import DataResponse, PredictionResponse

router = APIRouter()

@router.get("/data")
async def get_data():
    data_points = fetch_external_data()
    response = DataResponse(data=data_points)
    return response