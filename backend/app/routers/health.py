from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from db.session import get_db
from models.community import Community

router = APIRouter(prefix="/health")


@router.get(
    "",
    response_description="Health check",
    summary="Health check",
    status_code=200,
)
async def get_health(request: Request, db: Session = Depends(get_db)):
    try:
        # to check database we will execute raw query
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
