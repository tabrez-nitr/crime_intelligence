from __future__ import annotations

from datetime import date
from enum import Enum

from sqlalchemy import Date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.core.base import Base
from app.models.core.base import TimestampMixin


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Person(Base, TimestampMixin):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    gender: Mapped[Gender | None] = mapped_column(
        SQLEnum(Gender),
        nullable=True,
    )

    date_of_birth: Mapped[date | None] = mapped_column(
        Date,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
    )

    victims: Mapped[list["Victim"]] = relationship(
        back_populates="person",
    )

    accused_cases: Mapped[list["Accused"]] = relationship(
        back_populates="person",
    )

    complaints: Mapped[list["Complainant"]] = relationship(
        back_populates="person",
    )