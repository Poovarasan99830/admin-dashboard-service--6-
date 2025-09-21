# from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON
# from sqlalchemy.sql import func
# from src.common.database import Base

# class AuditLog(Base):
#     __tablename__ = "audit_logs"

#     log_id = Column(Integer, primary_key=True)
#     admin_id = Column(Integer, nullable=True)
#     action = Column(String(50), nullable=False)
#     entity_type = Column(String(50), nullable=False)
#     entity_id = Column(Integer, nullable=True)
#     details = Column(JSON, nullable=True)
#     timestamp = Column(TIMESTAMP, server_default=func.now())






import uuid
from sqlalchemy import Column, String, Enum, TIMESTAMP, JSON, text
from sqlalchemy.dialects.postgresql import UUID
import enum

from src.common.database import Base


class ActionType(str, enum.Enum):
    flagged_view = "flagged_view"
    dispute_resolved = "dispute_resolved"
    escalation = "escalation"
    notification_sent = "notification_sent"


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    admin_id = Column(UUID(as_uuid=True), nullable=False)
    action_type = Column(Enum(ActionType), nullable=False)
    target_id = Column(UUID(as_uuid=True), nullable=False)
    timestamp = Column(TIMESTAMP, server_default=text("now()"))
    extra_metadata = Column("metadata", JSON, nullable=True)  # <-- fixed
