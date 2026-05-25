import os

import pandas as pd

from config import STARTERS_CSV

_cache: pd.DataFrame | None = None
_mtime: float | None = None


def load_starters() -> pd.DataFrame:
    global _cache, _mtime
    mtime = os.path.getmtime(STARTERS_CSV)
    if _cache is None or mtime != _mtime:
        _cache = pd.read_csv(STARTERS_CSV, parse_dates=["date"])
        _mtime = mtime
    return _cache
