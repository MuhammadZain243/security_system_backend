from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    del app

    print("\nSecurity System Backend is running\n")
    print(f"API:          {settings.base_url}")
    print(f"Health:       {settings.base_url}/health")
    print(f"Swagger Docs: {settings.base_url}/docs")
    print(f"ReDoc:        {settings.base_url}/redoc")
    print()

    yield


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the Security System SaaS platform.",
    version=settings.app_version,
    lifespan=lifespan,
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": f"{settings.app_name} is running.",
        "version": settings.app_version,
        "environment": settings.app_env,
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }