from fastapi import APIRouter , Depends , status

from app.schemas.case import CaseCreate, CaseResponse
from app.services.case_service import CaseService
from app.services.dependencies import get_case_service


router = APIRouter(prefix="/cases" , tags=["Cases"])


@router.post(
    "/create",
    response_model=CaseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_case(data : CaseCreate , service : CaseService = Depends(get_case_service)):
    print("-" * 50)
    print()
    print("1 : INSIDE CREATE CASE ROUTE")
  

    return (
        service.create_case(
            data = data,
            created_by_id = 1 # temp until authentication added 
        )
    )
