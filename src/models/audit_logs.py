from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON
from sqlalchemy.sql import func
from src.common.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    log_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, nullable=True)
    action = Column(String(50), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(Integer, nullable=True)
    details = Column(JSON, nullable=True)
    timestamp = Column(TIMESTAMP, server_default=func.now())
