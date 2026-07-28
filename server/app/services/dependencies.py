from fastapi import Depends 
from sqlalchemy.orm import Session 

from app.db.dependencies import get_db
from app.repositories.case_repository import CaseRepository
from app.services.case_service import CaseService


def get_case_service(db:Session = Depends(get_db))-> CaseService:
    """ Get Case Service Object by creating repo and pass it to the case service"""
    
    repository = CaseRepository(db) # this will create obj and alsp set the session 

    return CaseService(repository)
    # we pass case service instance 