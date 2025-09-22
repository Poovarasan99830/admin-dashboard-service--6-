from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.sql import expression
from sqlalchemy.ext.declarative import declared_attr
from src.common.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    status = Column(String, nullable=False, default="active")  # active | suspended
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
