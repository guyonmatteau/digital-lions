from fastapi import FastAPI

from routers.workshop import router as workshop_router
from routers.user import router as user_router
from routers.health import router as health_router
from routers.attendance import router as attendance_router

app = FastAPI(title="Digital Lion API", version="0.1.0")

app.include_router(health_router, tags=["health"])
app.include_router(workshop_router, tags=["workshop"])
app.include_router(user_router, tags=["users"])
app.include_router(attendance_router, tags=["attendance"])


@app.on_event("startup")
async def startup_db_client():
    """On startup, ping the connection to the database"""
    pass

 
