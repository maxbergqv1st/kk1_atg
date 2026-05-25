from fastapi import APIRouter, HTTPException, Query

from app.schemas.horses import FormEntry
from app.services.horses import get_form

router = APIRouter(prefix="/api/horses", tags=["horses"])


@router.get("/{horse_name}/form", response_model=list[FormEntry])
def horse_form(horse_name: str, n: int = Query(default=10, ge=1, le=100)):
    entries = get_form(horse_name, n)
    if not entries:
        raise HTTPException(status_code=404, detail="Häst hittades inte")
    return entries
