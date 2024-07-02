import logging
import logging.config
import os
from contextlib import asynccontextmanager
from typing import Any

from dependencies.database import init_db
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import attendance, children, communities, health, teams, users, workshops

logging_conf = "logging.conf"
logging.config.fileConfig(logging_conf, disable_existing_loggers=False)  # type: ignore
logger = logging.getLogger(__name__)
logger.info("Logging configuration: %s", logging_conf)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")
methods = ["GET", "POST", "PUT", "DELETE"]
logger.info(f"CORSMiddleware allowed origins: {ALLOWED_ORIGINS}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """On startup, ping the connection to the database"""
    logger.info("Starting db client...")
    init_db()
    # logger.info("Running migrations...")
    # run_migrations()
    yield


async def catch_any_exception(request: Request, call_next: Any) -> Any:
    """Catch any exception and return it as 500 with info.
    TODO: this should be removed in production and handled by a proper error handler."""
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(e)
        return JSONResponse(status_code=500, content={"message": "Internal server error"})


app = FastAPI(title="Digital Lion's API", version="0.1.0", root_path="/api/v1", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=methods,
    allow_headers=["*"],
)
app.middleware("http")(catch_any_exception)
app.include_router(health.router, tags=["health"])
app.include_router(teams.router, tags=["teams"])
app.include_router(attendance.router, tags=["attendances"])
app.include_router(children.router, tags=["children"])
app.include_router(communities.router, tags=["communities"])
app.include_router(workshops.router, tags=["workshop"])
app.include_router(users.router, tags=["users"])
