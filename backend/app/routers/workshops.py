import exceptions
from dependencies.services import WorkshopServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.out import WorkshopOut

router = APIRouter(prefix="/workshops")


@router.get(
    "/{workshop_id}",
    summary="Get workshop by ID",
    status_code=status.HTTP_200_OK,
    response_model=WorkshopOut,
)
async def get_workshop(workshop_id: int, workshop_service: WorkshopServiceDependency):
    """Get a workshop by its ID."""
    try:
        return workshop_service.get(workshop_id)
    except exceptions.WorkshopNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workshop with ID {workshop_id} not found",
        )


@router.get(
    "",
    summary="Get workshops",
    status_code=status.HTTP_200_OK,
    response_model=list[WorkshopOut] | None,
)
async def get_workshops(
    workshop_service: WorkshopServiceDependency,
):
    """Get the Workshop of a child to a workshop."""
    return workshop_service.get_all()
