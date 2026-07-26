

from app.models.core.base import Base , TimestampMixin
from sqlalchemy import String , Integer , Boolean , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column , relationship

class GravityOffence(Base, TimestampMixin):

    """ Henious or non-henious case  """

    __tablename__ = "gravity_offences"

    id: Mapped[int] = mapped_column(primary_key=True)

    lookup_value: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )

    cases: Mapped[list["CaseMaster"]] = relationship(
        back_populates="gravity_offence"
    )