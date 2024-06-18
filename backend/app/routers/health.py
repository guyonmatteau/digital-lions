from dependencies.database import DatabaseDependency
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.community import Community

router = APIRouter(prefix="/health")


@router.get(
    "",
    response_description="Health check",
    summary="Health check",
    status_code=200,
)
async def get_health(db: DatabaseDependency):
    """Health endpoint for backend and databse."""
    try:
        # TODO use db.ping() to check for connection
        db.query(Community).first()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})
    except Exception as exc:
        if "psycopg2.OperationalError" in str(exc):
            output = "Database connection error"
        else:
            output = str(exc)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "error", "message": output},
        )
