from utils import load_starters

from app.schemas.horses import FormEntry

FORM_COLS = ["date", "track", "distance_m", "post_position",
             "finish_position", "odds", "race_time_sec", "won"]


def get_form(horse_name: str, n: int) -> list[FormEntry]:
    df = load_starters()
    active = df[~df["scratched"]]
    rows = (
        active[active["horse_name"] == horse_name]
        .sort_values("date", ascending=False)
        .head(n)[FORM_COLS]
        .copy()
    )
    rows["date"] = rows["date"].astype(str)
    return [FormEntry(**row) for row in rows.to_dict(orient="records")]
