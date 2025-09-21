import uuid
from sqlalchemy import Column, String, Enum, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum

from src.common.database import Base


class FlagStatus(str, enum.Enum):
    pending = "pending"
    reviewed = "reviewed"
    cleared = "cleared"


class FlaggedTransaction(Base):
    __tablename__ = "flagged_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    transaction_id = Column(UUID(as_uuid=True), nullable=False)
    flagged_reason = Column(String, nullable=False)
    flagged_at = Column(TIMESTAMP, server_default=text("now()"))
    status = Column(Enum(FlagStatus), nullable=False, default=FlagStatus.pending)

    disputes = relationship("PaymentDispute", back_populates="transaction")
