from fastapi import FastAPI
from oliveea.routers import healthcheck, craft


app = FastAPI()
app.include_router(healthcheck.router)
app.include_router(craft.router)