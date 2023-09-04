from fastapi import FastAPI
from functools import lru_cache
from .config import Settings
from .routers import healthcheck, craft


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI()
app.include_router(healthcheck.router)
app.include_router(craft.router)