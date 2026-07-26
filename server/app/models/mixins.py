from datetime import date

from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column


class PersonMixin:
    """Common fields shared by all people."""

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
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