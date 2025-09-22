# src/models/audit_logs.py

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.common.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs222"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    action = Column(String, nullable=False)   # e.g. dispute_resolved, flag_handled
    user_id = Column(UUID(as_uuid=True), nullable=False)  # ❌ removed ForeignKey("users.id")
    target_id = Column(UUID(as_uuid=True), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
