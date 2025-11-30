import { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000';

function App() {
  const [data, setData] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [features, setFeatures] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch data from GET endpoint
  const fetchData = async () => {
    setLoading(true);
    setError(null);
    setData(null);
    try {
      const response = await axios.get(`${API_URL}/api/v1/data`);
      setData(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  // Make prediction via POST endpoint
  const makePrediction = async () => {
    if (!features.trim()) {
      setError('Please enter features');
      return;
    }

    setLoading(true);
    setError(null);
    setPrediction(null);
    try {
      const featuresArray = features.split(',').map(f => parseFloat(f.trim()));
      
      if (featuresArray.some(isNaN)) {
        throw new Error('Invalid features. Use numbers separated by commas');
      }

      const response = await axios.post(`${API_URL}/api/v1/predict`, {
        features: featuresArray
      });
      setPrediction(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>ML Microservice Demo</h1>
        <p className="subtitle">Simple interface to interact with FastAPI backend</p>

        {/* Fetch Data Section */}
        <div className="card">
          <h2>Get Data</h2>
          <p className="description">Fetch list of numbers from GET /api/v1/data</p>
          <button onClick={fetchData} disabled={loading} className="btn">
            {loading ? 'Loading...' : 'Fetch Data'}
          </button>
          {data && (
            <div className="result success">
              <h3>Response:</h3>
              <pre>{JSON.stringify(data, null, 2)}</pre>
            </div>
          )}
        </div>

        {/* Prediction Section */}
        <div className="card">
          <h2>Make Prediction</h2>
          <p className="description">Send features to POST /api/v1/predict</p>
          <input
            type="text"
            value={features}
            onChange={(e) => setFeatures(e.target.value)}
            placeholder="Enter features (e.g., 1,2,3,4)"
            className="input"
          />
          <button onClick={makePrediction} disabled={loading} className="btn">
            {loading ? 'Predicting...' : 'Predict'}
          </button>
          {prediction && (
            <div className="result success">
              <h3>Prediction:</h3>
              <pre>{JSON.stringify(prediction, null, 2)}</pre>
            </div>
          )}
        </div>

        {/* Error Display */}
        {error && (
          <div className="result error">
            <strong>Error:</strong> {error}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;