from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from pydantic import BaseModel

from oliveea.core.crafter.crafter import Crafter
from oliveea.dependencies import get_crafter

router = APIRouter()


class CraftRequest(BaseModel):
    words: str
    tone: str


@router.post("/craft", tags=["craft"])
async def craft(
    craft_request: CraftRequest,
    crafter: Crafter = Depends(get_crafter),
):
    res = crafter.craft(
        words=craft_request.words,
        tone=craft_request.tone,
    )
    return res
