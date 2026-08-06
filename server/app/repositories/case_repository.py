from sqlalchemy.orm import Session 
from sqlalchemy import select , or_

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
    
    # dynamic search 
    def search_cases(
        self , 
        filters : CaseFilter,
        page : int , 
        page_size : int
    ):

        query = select(Case)

        if filters.search :
            query = query.where(
                or_(
                    Case.title.ilike(
                        f"%{filters.search}%"
                    ),
                    Case.description.ilike(
                        f"%{filters.search}%"
                    ),
                    Case.case_number.ilike(
                        f"%{filters.search}%"
                    ),
                )
            )
        
        if filters.crime_type_id : 

            query = query.where(
                Case.crime_type_id == filters.crime_type_id 
            )
        
        if filters.status : 

            query = query.where(
                Case.status == filters.status
            )
        
        if filters.priority : 

            query = query.where(
                Case.priority == filters.priority
            )
        
        query = query.offset(
            (page-1)*page_size
        )

        query = query.limit(page_size)

        return list(
            self.session.scalars(query)
        )
        
