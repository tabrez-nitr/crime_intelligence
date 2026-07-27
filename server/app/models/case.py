from __future__ import annotations

import enum
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    Text,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.base import TimestampMixin


class CaseStatus(str, enum.Enum):
    OPEN = "Open"
    UNDER_INVESTIGATION = "Under Investigation"
    CLOSED = "Closed"


class Priority(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class Case(Base, TimestampMixin):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    crime_type_id: Mapped[int] = mapped_column(
        ForeignKey("crime_types.id"),
        nullable=False,
    )

    status: Mapped[CaseStatus] = mapped_column(
        Enum(CaseStatus),
        default=CaseStatus.OPEN,
        nullable=False,
    )

    priority: Mapped[Priority] = mapped_column(
        Enum(Priority),
        default=Priority.MEDIUM,
        nullable=False,
    )

    incident_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    latitude: Mapped[float | None] = mapped_column(
        Numeric(9, 6)
    )

    longitude: Mapped[float | None] = mapped_column(
        Numeric(9, 6)
    )

    address: Mapped[str | None] = mapped_column(
        String(255)
    )

    reported_by: Mapped[str | None] = mapped_column(
        String(255)
    )

    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    created_by: Mapped["User"] = relationship(
        back_populates="cases"
    )

    crime_type: Mapped["CrimeType"] = relationship(
        back_populates="cases"
    )

    people: Mapped[list["CasePerson"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    evidence: Mapped[list["Evidence"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    laws: Mapped[list["CaseLaw"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    embeddings: Mapped[list["CaseEmbedding"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )