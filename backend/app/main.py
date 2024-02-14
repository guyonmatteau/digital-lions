from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers.workshop import workshop_router
from routers.user import user_router
from routers.health import health_router

app = FastAPI(title="Big Hippo API")

app.include_router(health_router, tags=["health"])
app.include_router(workshop_router, tags=["workshop"])
app.include_router(user_router, tags["user"])


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
