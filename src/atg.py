from datetime import date

import requests

from config import ATG_BASE, V_GAMES


def _get(url: str) -> dict:
    r = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_upcoming(day: date | None = None) -> list[dict]:
    if day is None:
        day = date.today()
    calendar = _get(f"{ATG_BASE}/calendar/day/{day}")
    rows = []
    for game_type, game_list in calendar.get("games", {}).items():
        if game_type not in V_GAMES:
            continue
        for stub in game_list:
            game = _get(f"{ATG_BASE}/games/{stub['id']}")
            for race in game.get("races", []):
                race_data = _get(f"{ATG_BASE}/races/{race['id']}")
                for start in race_data.get("starts", []):
                    horse = start.get("horse", {})
                    driver = start.get("driver", {})
                    rows.append({
                        "game_type": game_type,
                        "division": race_data.get("number"),
                        "track": (race_data.get("track") or {}).get("name"),
                        "horse_name": horse.get("name"),
                        "driver_name": f"{driver.get('firstName', '')} {driver.get('lastName', '')}".strip(),
                        "post_position": start.get("postPosition"),
                    })
    return rows
