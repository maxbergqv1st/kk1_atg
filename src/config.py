from pathlib import Path

ATG_BASE = "https://www.atg.se/services/racinginfo/v1/api"
STARTERS_CSV = Path(__file__).parent.parent / "data" / "processed" / "starters.csv"
V_GAMES = {"V64", "V75", "V85", "V86"}
