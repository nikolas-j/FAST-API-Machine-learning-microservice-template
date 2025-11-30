# Load / Build ML model on startup

from functools import lru_cache
from sklearn.cluster import DBSCAN

@lru_cache
def get_model():
    """Load a pre-trained ML model from the specified path."""
    # settings.MODEL_PATH <- path to model file
    model = DBSCAN(eps=15.0, min_samples=50)
    return model
    
