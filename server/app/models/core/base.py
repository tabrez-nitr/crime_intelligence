from datetime import datetime 

from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column
from sqlalchemy import DateTime , func



#this can be inherited to create new tables 
class Base(DeclarativeBase):
    """base class for all ORM models
    
    """
    pass 


# this class could be inherited to use created_at and updated_at 
class TimestampMixin:

    """
    this class is used to update the time of the created_at and updated_at
    when the value is updated 
    """

    created_at: Mapped[datetime] = mapped_column(
       DateTime(timezone=True),
        server_default=func.now(),
        nullable=False, #automatically updates the time 
        # now is sql query that returns the current time 
    
    )

    updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    server_onupdate=func.now(),
    onupdate=func.now(),
    nullable=False,
)

    
