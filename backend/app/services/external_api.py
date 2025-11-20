# Fetches data from external APIs
from app.core.config import get_settings
settings = get_settings()

URL = settings.EXTERNAL_API_URL
KEY = settings.API_KEY

def fetch_external_data():
    """Fetch data from an external API."""
    response = {"data": [1, 2, 3, 4, 5]}
    data_points = response["data"]
    return data_points