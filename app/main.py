"""Entry point for the sample real estate FastAPI application."""
from __future__ import annotations

from fastapi import FastAPI

from .routers import properties

app = FastAPI(title="Real Estate Sample API", version="0.1.0")
app.include_router(properties.router)


@app.get("/health", summary="Health check")
def health_check() -> dict[str, str]:
    """Simple endpoint for uptime checks."""

    return {"status": "ok"}
