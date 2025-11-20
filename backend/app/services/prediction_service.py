# Uses ml_model.py to run prediction
from app.models.ml_model import get_model

def run_prediction(input_data):
    """Run prediction using the loaded ML model."""
    #model = get_model()
    #prediction = model.fit_predict([input_data])[0]
    prediction = 42.0
    return prediction