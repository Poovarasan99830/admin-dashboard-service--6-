"""
CLI helper to create schema (via SQLAlchemy metadata.create_all) and insert sample rows.
Run: python scripts/seed_db.py
"""
from src.common.database import init_engine, get_engine, Base
from src.config.settings import settings
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from src.models.flagged_listings import FlaggedListing
from src.models.disputes import Dispute
from src.models.audit_logs import AuditLog

def main():
    engine = init_engine(settings.DATABASE_URL)
    Base.metadata.create_all(engine)  # create tables

    session = Session(bind=engine)
    # insert minimal sample records only if empty
    if not session.query(FlaggedListing).first():
        session.add_all([
            FlaggedListing(listing_id=5001, reason="Fake brand item", status="pending"),
            FlaggedListing(listing_id=5002, reason="Offensive content", status="reviewed")
        ])
    if not session.query(Dispute).first():
        session.add_all([
            Dispute(user_id=2, listing_id=5001, status="open"),
            Dispute(user_id=3, listing_id=5002, status="resolved")
        ])
    session.commit()
    session.close()
    print("DB seeded.")

if __name__ == "__main__":
    main()
