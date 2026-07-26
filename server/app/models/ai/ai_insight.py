from sqlalchemy import ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.core.base import Base, TimestampMixin


class AIInsight(Base, TimestampMixin):
    __tablename__ = "ai_insights"

    id: Mapped[int] = mapped_column(primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        nullable=False,
    )

    summary: Mapped[str] = mapped_column()

    entities: Mapped[dict] = mapped_column(
        JSONB,
        default=dict,
    )

    keywords: Mapped[list] = mapped_column(
        JSONB,
        default=list,
    )

    risk_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    similar_cases: Mapped[list] = mapped_column(
        JSONB,
        default=list,
    )

    case: Mapped["CaseMaster"] = relationship(
        back_populates="insights",
    )