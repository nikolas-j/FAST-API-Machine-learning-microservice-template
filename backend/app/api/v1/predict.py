# POST endpoint for making predictions

from fastapi import APIRouter, HTTPException
from app.services.prediction_service import run_prediction
from app.models.schemas import PredictionResponse

router = APIRouter()

@router.post("/predict")
async def make_prediction():
    model_out = run_prediction(input_data={})
    response = PredictionResponse(prediction=model_out)
    return response