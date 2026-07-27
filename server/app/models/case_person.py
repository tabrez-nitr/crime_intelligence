from __future__ import annotations

import enum

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PersonRole(str, enum.Enum):
    VICTIM = "Victim"
    ACCUSED = "Accused"
    WITNESS = "Witness"
    COMPLAINANT = "Complainant"
    OFFICER = "Officer"


class CasePerson(Base):
    __tablename__ = "case_persons"

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        primary_key=True,
    )

    person_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"),
        primary_key=True,
    )

    role: Mapped[PersonRole] = mapped_column(
        Enum(PersonRole),
        primary_key=True,
    )

    case: Mapped["Case"] = relationship(
        back_populates="people",
    )

    person: Mapped["Person"] = relationship(
        back_populates="cases",
    )