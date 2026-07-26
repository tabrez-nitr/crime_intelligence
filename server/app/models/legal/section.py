from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin


class Section(Base, TimestampMixin):
    __tablename__ = "sections"

    id: Mapped[int] = mapped_column(primary_key=True)

    act_id: Mapped[int] = mapped_column(
        ForeignKey("acts.id", ondelete="CASCADE"),
        nullable=False,
    )

    section_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    act: Mapped["Act"] = relationship(
        back_populates="sections",
    )

    cases: Mapped[list["CaseActSection"]] = relationship(
        back_populates="section",
        cascade="all, delete-orphan",
    )