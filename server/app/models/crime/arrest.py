from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin


class Arrest(Base, TimestampMixin):
    __tablename__ = "arrests"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    accused_id: Mapped[int] = mapped_column(
        ForeignKey("accused.id"),
        nullable=False,
    )

    officer_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        nullable=False,
    )

    arrest_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
    )

    case: Mapped["CaseMaster"] = relationship(
        back_populates="arrests",
    )

    accused: Mapped["Accused"] = relationship(
        back_populates="arrests",
    )

    officer: Mapped["Employee"] = relationship()