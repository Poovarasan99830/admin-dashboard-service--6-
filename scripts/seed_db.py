"""
CLI helper to create schema (via SQLAlchemy metadata.create_all) and insert sample rows.
Run: python scripts/seed_db.py
"""

import uuid
from sqlalchemy.orm import Session
from src.common.database import init_engine, get_engine, Base
from src.config.settings import settings
from src.models.flagged_listings import FlaggedListing
from src.models.disputes import Dispute
from src.models.audit_logs import AuditLog

# Initialize DB
engine = init_engine(settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)


def seed():
    with Session(engine) as session:
        # ✅ Seed flagged listings
        if not session.query(FlaggedListing).first():
            session.add_all([
                FlaggedListing(
                    id=uuid.uuid4(),
                    listing_id=5001,
                    reason="Fake brand item",
                    status="pending"
                ),
                FlaggedListing(
                    id=uuid.uuid4(),
                    listing_id=5002,
                    reason="Offensive content",
                    status="reviewed"
                )
            ])

        # ✅ Seed disputes
        if not session.query(Dispute).first():
            session.add_all([
                Dispute(
                    id=uuid.uuid4(),
                    user_id=uuid.uuid4(),
                    listing_id=5001,
                    status="open"
                ),
                Dispute(
                    id=uuid.uuid4(),
                    user_id=uuid.uuid4(),
                    listing_id=5002,
                    status="resolved"
                )
            ])

        # ✅ Seed audit logs
        if not session.query(AuditLog).first():
            session.add_all([
                AuditLog(
                    id=uuid.uuid4(),
                    action="dispute_resolved",
                    user_id=uuid.uuid4(),
                    target_id=uuid.uuid4()
                ),
                AuditLog(
                    id=uuid.uuid4(),
                    action="flag_handled",
                    user_id=uuid.uuid4(),
                    target_id=uuid.uuid4()
                )
            ])

        session.commit()
        print("✅ Database seeded with flagged listings, disputes, and audit logs")


if __name__ == "__main__":
    seed()
