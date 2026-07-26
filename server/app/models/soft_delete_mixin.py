from datetime import date, datetime
from sqlalchemy import Date, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class SoftDeleteMixin:
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    deleted_at: Mapped[datetime | None]