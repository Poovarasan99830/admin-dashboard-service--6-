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
