from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from src.common.database import Base
import enum

class ProviderStatus(str, enum.Enum):
    active = "active"
    suspended = "suspended"

class Provider(Base):
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Enum(ProviderStatus), default=ProviderStatus.active, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

