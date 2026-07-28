from __future__ import annotations

from typing import Generic , TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session 

from app.db.base import Base 

ModelType = TypeVar("ModelType" , bound=Base)
#"" internal name given to the type var 
# this is generic variabel which accepts any model with Base 

class BaseRepository(Generic[ModelType]):

    def __init__(
        self , 
        session : Session,
        model:type[ModelType]
    ): # this runs as soon as obj is made 

        self.session  = session
        self.model  = model 


    def add(self , obj : ModelType) -> ModelType:
        # recives obj model that is eqaul to modelType (all base models)
        """ this function adds obj to the db and returns back and object modelType """
        
        self.session.add(obj)
        return obj 
    
    def get(self , obj_id : int) -> ModelType | None :
        """ get the obj with the id from db  """

        return self.session.get(self.model , obj_id)


    def get_all(self) -> list[ModelType] | None :
        """ return all the obj from the db  """
        
        return list(
            self.session.scalars(
                select(self.model)
            ).all()
        )
        
    
    def delete(self , obj : ModelType) -> None:

        self.session.delete(obj)
    

    def commit(self) -> None:
        self.session.commit()
    
    def refresh(self , obj : ModelType) -> None:
        self.session.refresh(obj)
    
    def rollback(self) -> None:
        self.session.rollback()
        