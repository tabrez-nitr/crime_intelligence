from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin
from app.models.mixins import PersonMixin

class Complainant(Base, TimestampMixin):

    __tablename__ = "complainants"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        nullable=False,
    )

    person_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"),
        nullable=False,
    )

    statement: Mapped[str | None] = mapped_column(
        Text,
    )

    case = relationship(
        "CaseMaster",
        back_populates="complainants",
    )

    person = relationship(
        "Person",
        back_populates="complaints",
    )