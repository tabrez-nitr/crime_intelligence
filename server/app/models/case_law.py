from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CaseLaw(Base):
    __tablename__ = "case_laws"

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        primary_key=True,
    )

    law_id: Mapped[int] = mapped_column(
        ForeignKey("laws.id", ondelete="CASCADE"),
        primary_key=True,
    )

    case: Mapped["Case"] = relationship(
        back_populates="laws",
    )

    law: Mapped["Law"] = relationship(
        back_populates="cases",
    )