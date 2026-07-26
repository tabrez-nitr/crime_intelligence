from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin
from app.models.mixins import PersonMixin

class Victim(Base, TimestampMixin):

    __tablename__ = "victims"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        nullable=False,
    )

    person_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"),
        nullable=False,
    )

    injury_type: Mapped[str | None] = mapped_column(
        String(100),
    )

    statement: Mapped[str | None] = mapped_column(
        Text,
    )

    case = relationship(
        "CaseMaster",
        back_populates="victims",
    )

    person = relationship(
        "Person",
        back_populates="victims",
    )