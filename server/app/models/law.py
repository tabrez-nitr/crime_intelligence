from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Law(Base):
    """  """
    __tablename__ = "laws"

    id: Mapped[int] = mapped_column(primary_key=True)

    act: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    section: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    cases: Mapped[list["CaseLaw"]] = relationship(
        back_populates="law",
        cascade="all, delete-orphan",
    )