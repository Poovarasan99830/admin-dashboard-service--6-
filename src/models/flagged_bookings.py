from sqlalchemy import Column, Integer, String, Enum, DateTime, func, Text
from src.common.database import Base
import enum

class FlagStatus(str, enum.Enum):
    pending = "pending"
    reviewed = "reviewed"
    resolved = "resolved"

class FlaggedBooking(Base):
    __tablename__ = "flagged_bookings"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)
    reason = Column(Text, nullable=False)
    status = Column(Enum(FlagStatus), default=FlagStatus.pending, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)
