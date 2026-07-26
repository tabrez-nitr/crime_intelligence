from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin


class Evidence(Base, TimestampMixin):
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    file_url: Mapped[str | None] = mapped_column(
        String(500),
    )

    collected_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("employees.id"),
    )

    collected_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    case: Mapped["CaseMaster"] = relationship(
        back_populates="evidence",
    )

    collected_by: Mapped["Employee | None"] = relationship()