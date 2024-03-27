from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers.workshop import router as workshop_router
from routers.user import router as user_router
from routers.health import router as health_router

app = FastAPI(title="Digital Lion API", version="0.1.0")

@app.on_event("startup")
def startup_db_client():
    pass

app.include_router(health_router, tags=["health"])
app.include_router(workshop_router, tags=["workshop"])
app.include_router(user_router, tags=["users"])
