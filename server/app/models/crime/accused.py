from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin

class Accused(Base, TimestampMixin):

    __tablename__ = "accused"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        nullable=False,
    )

    person_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"),
        nullable=False,
    )

    status: Mapped[str | None] = mapped_column(
        String(50),
    )

    is_repeat_offender: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    criminal_history: Mapped[str | None] = mapped_column(
        Text,
    )

    case = relationship(
        "CaseMaster",
        back_populates="accused",
    )

    person = relationship(
        "Person",
        back_populates="accused_cases",
    )

    arrests = relationship(
        "Arrest",
        back_populates="accused",
    )