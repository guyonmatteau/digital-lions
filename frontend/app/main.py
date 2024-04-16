from fastapi import FastAPI
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.responses import RedirectResponse

import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", name="index")
async def index(request: Request):
    return RedirectResponse(url="/home")

@app.get("/home", name="home")
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/attendance", name="attendance")
async def attendance(request: Request):
    return templates.TemplateResponse("attendance.html", {"request": request})


@app.get("/children", name="children")
async def children(request: Request):
    return templates.TemplateResponse("children.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
