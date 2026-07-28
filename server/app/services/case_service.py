from app.models.case import Case
from app.repository.case_repository import CaseRepository 

from uuid import uuid4

from app.schemas.case import CaseCreate 



class CaseService:

    def __init__(self , repository : CaseRepository):

        self.repository = repository

    
    def create_case(self , data : CaseCreate , created_by_id : int) -> Case:
        """ Create New Case  """

        case = Case(
            **data.model_dump(),
            case_number = self.generate_case_number(),
            created_by_id = created_by_id
        )

        self.repository.add(case)
        self.repository.commit()
        self.repository.refresh(case)

        return case 
        # case is passed as obj 

    
    def generate_case_number(self) -> str :

        return f"CR-{uuid4().hex[:8].upper()}"

    
    def get_case(self , case : Case ) -> list[Case]:
        """ return all cases """
        return self.repository.get_all()
    
    def delete_case(self , case:Case )-> None:
        """ Delete Case  """

        self.repository.delete(case)