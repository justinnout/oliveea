from fastapi import APIRouter

router = APIRouter()

@router.get("/health/liveness", tags=["healthcheck"])
async def health_liveness():
    return "OK"

@router.get("/health/readiness", tags=["healthcheck"])
async def health_readiness():
    return "OK"
