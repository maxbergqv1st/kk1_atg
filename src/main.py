from fastapi import FastAPI
from fastapi.responses import FileResponse

from routers import horses, races

app = FastAPI(title="ATG Travanalys")

app.include_router(races.router)
app.include_router(horses.router)


@app.get("/", response_class=FileResponse)
def index():
    return FileResponse("src/static/index.html")
