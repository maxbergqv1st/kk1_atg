from pydantic import BaseModel


class FormEntry(BaseModel):
    date: str
    track: str | None
    distance_m: int | None
    post_position: int | None
    finish_position: int | None
    odds: float | None
    race_time_sec: float | None
    won: bool
