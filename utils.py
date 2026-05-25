import os
import requests
import pandas as pd
from pathlib import Path
from datetime import date

BASE          = "https://www.atg.se/services/racinginfo/v1/api"
ROOT          = Path(__file__).parent
PROCESSED_DIR = ROOT / "data" / "processed"

V_GAMES = {"V64", "V75", "V85", "V86"}


def fetch(url):
    r = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_upcoming(day=None):
    if day is None:
        day = date.today()
    if isinstance(day, str):
        day = date.fromisoformat(day)
    calendar = fetch(f"{BASE}/calendar/day/{day}")
    rows = []
    for game_type, game_list in calendar.get("games", {}).items():
        if game_type not in V_GAMES:
            continue
        for game_stub in game_list:
            game = fetch(f"{BASE}/games/{game_stub['id']}")
            for race in game.get("races", []):
                race_data = fetch(f"{BASE}/races/{race['id']}")
                for start in race_data.get("starts", []):
                    horse  = start.get("horse", {})
                    driver = start.get("driver", {})
                    rows.append({
                        "game_type":     game_type,
                        "division":      race_data.get("number"),
                        "track":         (race_data.get("track") or {}).get("name"),
                        "horse_name":    horse.get("name"),
                        "driver_name":   driver.get("firstName", "") + " " + driver.get("lastName", ""),
                        "post_position": start.get("postPosition"),
                    })
    cols = ["game_type", "division", "track", "horse_name", "driver_name", "post_position"]
    return pd.DataFrame(rows, columns=cols) if rows else pd.DataFrame(columns=cols)


_starters_cache = None
_starters_mtime = None


def load_starters() -> pd.DataFrame:
    global _starters_cache, _starters_mtime
    path = PROCESSED_DIR / "starters.csv"
    mtime = os.path.getmtime(path)
    if _starters_cache is None or mtime != _starters_mtime:
        _starters_cache = pd.read_csv(path, parse_dates=["date"])
        _starters_mtime = mtime
    return _starters_cache
