from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin


class Act(Base, TimestampMixin):
    __tablename__ = "acts"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    sections: Mapped[list["Section"]] = relationship(
        back_populates="act",
        cascade="all, delete-orphan",
    )