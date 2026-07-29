from sqlalchemy.orm import Session 
from sqlalchemy import select

from app.models.case import Case
from app.repositories.base import BaseRepository 




class CaseRepository(BaseRepository[Case]):
    """ Inherit Baserepository functions  """

    def __init__(self , session : Session):
        super().__init__(session , Case)
        # super passes this to the parent classs from extending class 
    
    def get_by_case_number(
        self , case_number : str 
    )-> Case | None :

       

        return self.session.scalar(
            select(Case).where(
                Case.case_number == case_number
                )
        )
        
