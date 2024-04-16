from fastapi import FastAPI
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/attendance")
def home(request: Request):
    return templates.TemplateResponse("attendance.html", {"request": request})


@app.get("/children")
def home(request: Request):
    return templates.TemplateResponse("children.html", {"request": request})


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
