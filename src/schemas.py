from pydantic import BaseModel


class Starter(BaseModel):
    game_type: str | None
    division: int | None
    track: str | None
    horse_name: str | None
    driver_name: str | None
    post_position: int | None


class FormEntry(BaseModel):
    date: str
    track: str | None
    distance_m: int | None
    post_position: int | None
    finish_position: int | None
    odds: float | None
    race_time_sec: float | None
    won: bool
