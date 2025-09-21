from sqlalchemy import Column, Integer, Enum, DateTime, Text, func
from src.common.database import Base
import enum

class AdminActionType(str, enum.Enum):
    suspend = "suspend"
    restore = "restore"

class AdminAction(Base):
    __tablename__ = "admin_actions"
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)
    action = Column(Enum(AdminActionType), nullable=False)
    reason = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
