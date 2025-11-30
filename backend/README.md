# Backend

FAST API based machine learning microservice backend template.

## Key Benefits

- **Clear separation of concerns:** API endpoints, business logic, and data models are properly organized
- **API versioning:** Built-in support for versioned endpoints (v1, v2, etc.)
- **Docker-ready:** Containerized deployment with Docker Compose for easy scaling
- **Environment-based config:** Secure configuration management with Pydantic Settings
- **Auto-generated docs:** Interactive API documentation via FastAPI's built-in Swagger/OpenAPI
- **Type safety:** Full type checking with Pydantic for request/response validation

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Docker (optional, for containerized deployment)

## Installation

### Option 1: Using uv (Recommended)

```powershell
# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
uv pip install -e .
```

### Option 2: Using pip

```powershell
# Create virtual environment
python -m venv .venv

# Activate
.venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Configuration

Create a `.env` file in the backend directory:

```env
APP_NAME=app-name
DEBUG=False
EXTERNAL_API_URL=https://api.example.com
API_KEY=key-here
DATABASE_URL=url-here
ALLOWED_ORIGINS=["http://localhost:8000"]
```

## Running Locally

```powershell
# Development mode (with auto-reload)
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Visit:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## Running with Docker

### Build the image and run

```powershell
docker-compose up
```

Visti: 
- API: http://localhost:8000
- Docs: http://localhost:8000/docs


