# FAST API Machine Learning Microservice Template

A prototyping-ready boilerplate for building ML microservices with FastAPI and React.

## Overview

This template provides a complete fullstack setup for deploying machine learning models as REST APIs with a clean, modern web interface. Perfect for quickly prototyping and productionizing ML applications.

**Stack:**
- **Backend:** FastAPI + Python
- **Frontend:** React + Vite
- **Containerization:** Docker + Docker Compose
- **Package Management:** uv (backend), npm (frontend)

## Project Structure

```
ml-fullstack-demo/
├── backend/              # FastAPI ML microservice
│   ├── app/
│   │   ├── api/v1/      # API endpoints
│   │   ├── core/        # Configuration
│   │   ├── models/      # Pydantic schemas
│   │   └── services/    # Business logic
│   ├── ml_models        # Store models / Load from registry
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── pyproject.toml
│   └── README.md        # Backend setup instructions
├── frontend/            # React web interface
│   ├── src/
│   ├── package.json
│   └── README.md        # Frontend setup instructions
└── README.md            # This file
```

## Quick Start

### Backend

```powershell
cd backend
# See backend/README.md for detailed setup
docker-compose up
```

Backend API will be available at:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

### Frontend

```powershell
cd frontend
# See frontend/README.md for detailed setup
npm install
npm run dev
```

Frontend will be available at http://localhost:3000

## Features

### Backend
- FastAPI with automatic OpenAPI documentation
- Pydantic for data validation
- Docker containerization
- Environment-based configuration
- RESTful API structure
- CORS enabled for frontend integration

### Frontend
- React 18 with Vite
- Minimalist, responsive UI
- Axios for API calls
- Error handling and loading states
- Chart.js ready for visualizations

### API Endpoints

- `GET /api/v1/data` - Fetch sample data
- `POST /api/v1/predict` - Make predictions

See http://localhost:8000/docs for full API documentation.

## Use Cases

This template is ideal for:
- 🤖 Deploying ML models as REST APIs
- 📊 Creating interactive ML demos
- 🚀 Rapid prototyping of ML applications
- 🏗️ Building production ML microservices
- 📈 Visualizing model predictions and data

## Configuration

### Backend
Configure via `.env` file in `backend/`:
```env
APP_NAME=App name
DATABASE_URL=url-here
API_KEY=key-here
ALLOWED_ORIGINS=http://example.com
```

### Frontend
API URL is configured in `frontend/src/App.jsx`:
```javascript
const API_URL = 'http://localhost:8000';
```

## Extending the Template

1. **Add ML models:** Place trained models in `backend/ml_models/`
2. **Create endpoints:** Add routes in `backend/app/api/v1/`
3. **Add services:** Implement logic in `backend/app/services/`
4. **Update UI:** Modify React components in `frontend/src/`
5. **Add visualizations:** Use Chart.js via `react-chartjs-2`


## License

MIT

## Contributing

This is a template project - feel free to fork and customize for your needs.

