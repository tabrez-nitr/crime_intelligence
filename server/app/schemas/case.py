from datetime import datetime 

from pydantic import BaseModel , ConfigDict 

from app.models.case import CaseStatus , Priority

class CaseBase(BaseModel):
    title: str
    description: str
    crime_type_id: int

    status: CaseStatus = CaseStatus.OPEN
    priority: Priority = Priority.MEDIUM

    incident_date: datetime

    latitude: float | None = None
    longitude: float | None = None

    address: str | None = None

    reported_by: str | None = None  





class CaseCreate(CaseBase):
    pass



class CaseUpdate(BaseModel):

    title: str | None = None
    description: str | None = None

    status: CaseStatus | None = None

    priority: Priority | None = None

    address: str | None = None

    latitude: float | None = None
    longitude: float | None = None


class CaseResponse(CaseBase):

    id: int

    case_number: str

    created_by_id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True 
    )# this helps to read objects 
    # by default pydantic reqads dict 
    