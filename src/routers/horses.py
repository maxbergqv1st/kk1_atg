from fastapi import APIRouter, HTTPException, Query

from schemas import FormEntry
from starters import load_starters

router = APIRouter(prefix="/api/horses", tags=["horses"])

_FORM_COLS = ["date", "track", "distance_m", "post_position",
              "finish_position", "odds", "race_time_sec", "won"]


@router.get("/{horse_name}/form", response_model=list[FormEntry])
def horse_form(horse_name: str, n: int = Query(default=10, ge=1, le=100)):
    df = load_starters()
    rows = (
        df[~df["scratched"] & (df["horse_name"] == horse_name)]
        .sort_values("date", ascending=False)
        .head(n)[_FORM_COLS]
        .copy()
    )
    if rows.empty:
        raise HTTPException(status_code=404, detail="Häst hittades inte")
    rows["date"] = rows["date"].astype(str)
    return rows.to_dict(orient="records")
