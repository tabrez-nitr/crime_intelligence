from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base


class CaseActSection(Base):
    __tablename__ = "case_act_sections"

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        primary_key=True,
    )

    section_id: Mapped[int] = mapped_column(
        ForeignKey("sections.id", ondelete="CASCADE"),
        primary_key=True,
    )

    case: Mapped["CaseMaster"] = relationship(
        back_populates="act_sections",
    )

    section: Mapped["Section"] = relationship(
        back_populates="cases",
    )