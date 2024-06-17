import logging
import logging.config
import os

from dependencies.database import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from routers.attendance import router as attendance_router
from routers.children import router as child_router
from routers.communities import router as community_router
from routers.health import router as health_router
from routers.teams import router as teams_router

# from routers.user import router as user_router
# from routers.workshop import router as workshop_router

logging_conf = "logging.conf"
logging.config.fileConfig(logging_conf, disable_existing_loggers=False)  # type: ignore
logger = logging.getLogger(__name__)
logger.info("Logging configuration: %s", logging_conf)

app = FastAPI(title="Digital Lion API", version="0.1.0", root_path="/api/v1")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")
methods = ["GET", "POST", "PUT", "DELETE"]
logger.info(f"CORSMiddleware allowed rigins: {ALLOWED_ORIGINS}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=methods,
    allow_headers=["*"],
)

app.include_router(health_router, tags=["health"])
app.include_router(teams_router, tags=["teams"])
# app.include_router(attendance_router, tags=["attendances"])
app.include_router(child_router, tags=["children"])
app.include_router(community_router, tags=["communities"])
# app.include_router(workshop_router, tags=["workshop"])
# app.include_router(user_router, tags=["users"])


@app.on_event("startup")
async def startup_db_client():
    """On startup, ping the connection to the database"""
    logger.info("Starting db client...")
    init_db()
    # logger.info("Running migrations...")
    # run_migrations()
