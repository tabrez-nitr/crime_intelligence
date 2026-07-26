from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.core.base import Base
from app.models.core.base import TimestampMixin



class CaseMaster(Base, TimestampMixin):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True)

    crime_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    case_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    case_title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    brief_facts: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    crime_registered_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    incident_from: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    incident_to: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
    )

    latitude: Mapped[float | None] = mapped_column(
        Numeric(10, 7),
    )

    longitude: Mapped[float | None] = mapped_column(
        Numeric(10, 7),
    )

    case_category_id: Mapped[int] = mapped_column(
        ForeignKey("case_categories.id"),
        nullable=False,
    )

    case_status_id: Mapped[int] = mapped_column(
        ForeignKey("case_statuses.id"),
        nullable=False,
    )

    crime_head_id: Mapped[int] = mapped_column(
        ForeignKey("crime_heads.id"),
        nullable=False,
    )

    crime_sub_head_id: Mapped[int] = mapped_column(
        ForeignKey("crime_sub_heads.id"),
        nullable=False,
    )

    gravity_offence_id: Mapped[int] = mapped_column(
        ForeignKey("gravity_offences.id"),
        nullable=False,
    )

    unit_id: Mapped[int] = mapped_column(
        ForeignKey("units.id"),
        nullable=False,
    )

    investigating_officer_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        nullable=False,
    )

    court_id: Mapped[int | None] = mapped_column(
        ForeignKey("courts.id"),
    )

    # Relationships

    case_category: Mapped["CaseCategory"] = relationship(
        back_populates="cases",
    )

    case_status: Mapped["CaseStatus"] = relationship(
        back_populates="cases",
    )

    crime_head: Mapped["CrimeHead"] = relationship(
        back_populates="cases",
    )

    crime_sub_head: Mapped["CrimeSubHead"] = relationship(
        back_populates="cases",
    )

    gravity_offence: Mapped["GravityOffence"] = relationship(
        back_populates="cases",
    )

    unit: Mapped["Unit"] = relationship(
        back_populates="cases",
    )

    investigating_officer: Mapped["Employee"] = relationship(
        back_populates="cases",
    )

    court: Mapped["Court | None"] = relationship(
        back_populates="cases",
    )

    victims: Mapped[list["Victim"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    accused: Mapped[list["Accused"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    complainants: Mapped[list["Complainant"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    evidence: Mapped[list["Evidence"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    arrests: Mapped[list["Arrest"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    act_sections: Mapped[list["CaseActSection"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    embeddings: Mapped[list["CaseEmbedding"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    insights: Mapped[list["AIInsight"]] = relationship(
        back_populates="case",
        cascade="all, delete-orphan",
    )

    priority: Mapped[str] = mapped_column(
    String(20),
    default="medium",
)

    is_sensitive: Mapped[bool] = mapped_column(
    default=False,
)

    embeddings: Mapped[list["CaseEmbedding"]] = relationship(
    back_populates="case",
    cascade="all, delete-orphan",
)
    content: Mapped[str] = mapped_column(
    Text,
    nullable=False,
)