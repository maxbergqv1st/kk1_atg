from datetime import date

from utils import fetch_upcoming

from app.schemas.races import Starter


def get_upcoming(day: date | None) -> list[Starter]:
    df = fetch_upcoming(day=day)
    return [Starter(**row) for row in df.to_dict(orient="records")]
