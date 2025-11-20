# Schemas for request and response models

from pydantic import BaseModel

class DataResponse(BaseModel):
    data: list[float]
    
class PredictionResponse(BaseModel):
    prediction: float
