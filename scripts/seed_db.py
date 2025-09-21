# """
# CLI helper to create schema (via SQLAlchemy metadata.create_all) and insert sample rows.
# Run: python scripts/seed_db.py
# """
# from src.common.database import init_engine, get_engine, Base
# from src.config.settings import settings
# from sqlalchemy import inspect
# from sqlalchemy.orm import Session
# from src.models.flagged_listings import FlaggedListing
# from src.models.disputes import Dispute
# from src.models.audit_logs import AuditLog

# def main():
#     engine = init_engine(settings.DATABASE_URL)
#     Base.metadata.create_all(engine)  # create tables

#     session = Session(bind=engine)
#     # insert minimal sample records only if empty
#     if not session.query(FlaggedListing).first():
#         session.add_all([
#             FlaggedListing(listing_id=5001, reason="Fake brand item", status="pending"),
#             FlaggedListing(listing_id=5002, reason="Offensive content", status="reviewed")
#         ])
#     if not session.query(Dispute).first():
#         session.add_all([
#             Dispute(user_id=2, listing_id=5001, status="open"),
#             Dispute(user_id=3, listing_id=5002, status="resolved")
#         ])
#     session.commit()
#     session.close()
#     print("DB seeded.")

# if __name__ == "__main__":
#     main()



# import sys, os
# from pathlib import Path

# # ensure src/ is on the Python path
# BASE_DIR = Path(__file__).resolve().parent.parent
# sys.path.append(str(BASE_DIR))

# from src.common.database import SessionLocal, engine, Base
# from src.models.providers import Provider
# from src.models.flagged_bookings import FlaggedBooking, FlagStatus
# from src.common.database import Base

# def seed():
#     Base.metadata.create_all(bind=engine)
#     db = SessionLocal()
#     # clear existing (dev only)
#     try:
#         db.query(FlaggedBooking).delete()
#         db.query(Provider).delete()
#         db.commit()
#     except Exception:
#         db.rollback()
#     p1 = Provider(id=501, name="Provider One", status="active")
#     p2 = Provider(id=502, name="Provider Two", status="active")
#     db.add_all([p1, p2])
#     db.flush()
#     f1 = FlaggedBooking(booking_id=9001, provider_id=501, reason="Customer reported harassment", status=FlagStatus.pending)
#     f2 = FlaggedBooking(booking_id=9002, provider_id=502, reason="Suspected fraud", status=FlagStatus.pending)
#     db.add_all([f1, f2])
#     db.commit()
#     print("Seeded DB with sample providers and flagged bookings")
#     db.close()

# if __name__ == "__main__":
#     seed()


"""
CLI helper to create schema (via SQLAlchemy metadata.create_all) and insert sample rows.
Run:  python scripts/seed_db.py
"""

import sys
from pathlib import Path

# ensure src/ is on the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.common.database import SessionLocal, engine, Base
from src.models.providers import Provider, ProviderStatus
from src.models.flagged_bookings import FlaggedBooking, FlagStatus
from src.models.flagged_listings import FlaggedListing
from src.models.disputes import Dispute


def seed():
    # create schema if not exists
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # clear existing rows (dev only)
        db.query(FlaggedBooking).delete()
        db.query(FlaggedListing).delete()
        db.query(Dispute).delete()
        db.query(Provider).delete()
        db.commit()
    except Exception:
        db.rollback()

    # --- Providers ---
    p1 = Provider(id=501, name="Provider One", status=ProviderStatus.active)
    p2 = Provider(id=502, name="Provider Two", status=ProviderStatus.active)
    db.add_all([p1, p2])
    db.flush()

    # --- Flagged Bookings (Services Squad) ---
    f1 = FlaggedBooking(
        booking_id=9001,
        provider_id=501,
        reason="Customer reported harassment",
        status=FlagStatus.pending,
    )
    f2 = FlaggedBooking(
        booking_id=9002,
        provider_id=502,
        reason="Suspected fraud",
        status=FlagStatus.pending,
    )
    db.add_all([f1, f2])

    # --- Flagged Listings (Marketplace Squad) ---
    l1 = FlaggedListing(
        listing_id=5001,
        reason="Fake brand item",
        status="pending",
    )
    l2 = FlaggedListing(
        listing_id=5002,
        reason="Offensive content",
        status="reviewed",
    )
    db.add_all([l1, l2])

    # --- Disputes (Marketplace Squad) ---
    d1 = Dispute(user_id=2, listing_id=5001, status="open")
    d2 = Dispute(user_id=3, listing_id=5002, status="resolved")
    db.add_all([d1, d2])

    # commit everything
    db.commit()
    db.close()
    print("✅ Seeded DB with providers, flagged bookings, flagged listings, and disputes.")


if __name__ == "__main__":
    seed()
