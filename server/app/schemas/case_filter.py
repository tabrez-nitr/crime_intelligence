from pydantic import BaseModel

from app.models.case import CaseStatus , Priority


class CaseFilter(BaseModel):

    search : str | None = None 

    crime_type_id : int | None = None 

    status : CaseStatus | None = None 

    priority : Priority | None = None 

    