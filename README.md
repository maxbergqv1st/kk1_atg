# ATG 

source .venv/bin/activate
uvicorn src.main:app --reload


PYTHONPATH=src uvicorn src.main:app --reload