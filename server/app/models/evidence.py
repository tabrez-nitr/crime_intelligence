from __future__ import annotations

import enum

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class EvidenceType(str, enum.Enum):
    DOCUMENT = "Document"
    IMAGE = "Image"
    VIDEO = "Video"
    AUDIO = "Audio"
    WEAPON = "Weapon"
    FINGERPRINT = "Fingerprint"
    DNA = "DNA"
    OTHER = "Other"


class Evidence(Base, TimestampMixin):
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    #case id to attach the evidence 
    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    # cascase -> delete all the evidence if parent case is deleted  

    type: Mapped[EvidenceType] = mapped_column(
        Enum(EvidenceType),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    file_url: Mapped[str | None] = mapped_column(
        String(500),
    )

    case: Mapped["Case"] = relationship(
        back_populates="evidence",
    )