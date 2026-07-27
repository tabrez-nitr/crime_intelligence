from __future__ import annotations

import enum

from sqlalchemy import Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin

# Gender Enum
class Gender(str, enum.Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Person(Base, TimestampMixin):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    gender: Mapped[Gender] = mapped_column(
        Enum(Gender),
        nullable=False,
    )

    age: Mapped[int | None] = mapped_column(
        Integer,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
    )

    cases: Mapped[list["CasePerson"]] = relationship(
        back_populates="person",
        cascade="all, delete-orphan",
    ) 
    # in how many cases this indivual is involved in 