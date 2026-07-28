from app.models.case import Case
from app.repository.case_repository import CaseRepository 



class CaseService:

    def __init__(self , repository : CaseRepository):

        self.repository = repository

    
    def create_case(self , case: Case) -> Case:
        """ Create New Case  """

        return self.repository.create(case) 
        # case is passed as obj 

    
    def get_case(self , case : Case ) -> list[Case]:
        """ return all cases """
        return self.repository.get_all()
    
    def delete_case(self , case:Case )-> None:
        """ Delete Case  """

        self.repository.delete(case)