# Real-Estate-Data

Sample FastAPI backend for experimenting with real estate datasets and API workflows.

## Features

- In-memory catalog of residential properties with detailed metadata
- REST endpoints for listing properties, retrieving individual records, and generating market summaries
- Typed Pydantic schemas for easy integration with AI assistants or frontend apps
- Automated tests using FastAPI's TestClient

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API locally:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Explore the interactive docs at http://127.0.0.1:8000/docs

## Running Tests

```bash
pytest
```
