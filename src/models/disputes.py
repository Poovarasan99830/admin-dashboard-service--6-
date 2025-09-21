from sqlalchemy import Column, Integer, Text, String, TIMESTAMP
from sqlalchemy.sql import func
from src.common.database import Base

class Dispute(Base):
    __tablename__ = "disputes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    listing_id = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, server_default="open")  # open|in_review|resolved
    created_at = Column(TIMESTAMP, server_default=func.now())
    resolved_at = Column(TIMESTAMP, nullable=True)
    resolved_by = Column(Integer, nullable=True)
    resolution_notes = Column(Text, nullable=True)






import uuid
from sqlalchemy import Column, String, Enum, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum

from src.common.database import Base


class DisputeStatus(str, enum.Enum):
    open = "open"
    under_review = "under_review"
    resolved = "resolved"
    escalated = "escalated"







class PaymentDispute(Base):
    __tablename__ = "payment_disputes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    transaction_id = Column(UUID(as_uuid=True), ForeignKey("flagged_transactions.id"))
    user_id = Column(UUID(as_uuid=True), nullable=False)
    dispute_reason = Column(String, nullable=False)
    status = Column(Enum(DisputeStatus), default=DisputeStatus.open)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    resolved_at = Column(TIMESTAMP, nullable=True)

    transaction = relationship("FlaggedTransaction", back_populates="disputes")
