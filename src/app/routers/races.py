from datetime import date

from fastapi import APIRouter, HTTPException

from app.schemas.races import Starter
from app.services.races import get_upcoming

router = APIRouter(prefix="/api/races", tags=["races"])


@router.get("/upcoming", response_model=list[Starter])
def upcoming(day: date | None = None):
    try:
        return get_upcoming(day)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
