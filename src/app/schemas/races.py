from pydantic import BaseModel


class Starter(BaseModel):
    game_type: str | None
    division: int | None
    track: str | None
    horse_name: str | None
    driver_name: str | None
    post_position: int | None
