from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from oliveea.core.crafter.crafter import Crafter

router = APIRouter()

class CraftRequest(BaseModel):
    words: str
    tone: str

@router.post("/craft", tags=["craft"])
async def craft(
    craft_request: CraftRequest,
    crafter: Annotated[Crafter, Depends(Crafter)]
):
    crafter.craft(
        words=craft_request.words,
        tone=craft_request.tone
    )
    return craft_request
