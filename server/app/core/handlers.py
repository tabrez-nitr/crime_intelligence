from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    AppException ,
    ConflictException,
    NotFoundException
)

def register_exception_handlers(app : FastAPI):
    """ reccives fastAPI app  """

    #if any one calls NotFoundException run the below func of this decorator 
    @app.exception_handler(NotFoundException)
    async def not_found(_ , exc):
        #  request , exc is exception 
        # we wrote _ this beacuse we are not usign request here 

        return JSONResponse(
            status_code=404,
            content={
                "detail" : str(exc)
            },
        )
