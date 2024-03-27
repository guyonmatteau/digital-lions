from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/health")


@router.get(
    "", response_description="Health check", summary="Health check", status_code=200
)
async def get_health(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})
