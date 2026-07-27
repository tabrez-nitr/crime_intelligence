from sqlalchemy.orm import Session 

from app.models.case import Case
from app.repositories.base import BaseRepository 


class CaseRepository(BaseRepository[Case]):
    """ Inherit Baserepository functions  """

    def __init__(self , session : Session):
        super().__init__(session , Case)
        # super passes this to the parent classs from extending class 
        
