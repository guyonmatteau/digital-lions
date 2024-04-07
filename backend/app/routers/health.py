from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from db.session import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session


router = APIRouter(prefix="/health")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "", response_description="Health check", summary="Health check", status_code=200, 
)
async def get_health(request: Request, db: Session = Depends(get_db)):
    output = 'database is ok'

    try:
        # to check database we will execute raw query
        db.execute('SELECT 1')
        return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})
    except Exception as exc:
        output = str(exc)
        return JSONResponse(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content={"status": "error", "message": output})
