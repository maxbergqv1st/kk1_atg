from datetime import date

from fastapi import APIRouter, HTTPException

from atg import fetch_upcoming
from schemas import Starter

router = APIRouter(prefix="/api/races", tags=["races"])


@router.get("/upcoming", response_model=list[Starter])
def upcoming(day: date | None = None):
    try:
        return fetch_upcoming(day)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
