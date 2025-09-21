from sqlalchemy import Column, Integer, Text, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from src.common.database import Base

class FlaggedListing(Base):
    __tablename__ = "flagged_listings"

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, nullable=False)  # can be FK marketplace_listings(listing_id) if exists
    reason = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, server_default="pending")  # pending|reviewed|resolved
    created_at = Column(TIMESTAMP, server_default=func.now())
    resolved_at = Column(TIMESTAMP, nullable=True)
    resolved_by = Column(Integer, nullable=True)  # admin id
