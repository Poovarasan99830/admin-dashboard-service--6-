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

# """
# CLI helper to create schema and insert sample rows.
# Run: python -m scripts.seed_db
# """
# import uuid
# from sqlalchemy.orm import Session

# from src.common.database import init_engine, get_engine, Base
# from src.config.settings import settings
# from src.models.admin_flags import FlaggedTransaction
# from src.models.disputes import PaymentDispute
# from src.models.audit_logs import AuditLog, ActionType


# # Initialize DB using project settings
# init_engine(settings.DATABASE_URL)
# engine = get_engine()
# Base.metadata.create_all(bind=engine)


# def seed():
#     with Session(engine) as db:
#         txn_id = uuid.uuid4()

#         flagged = FlaggedTransaction(
#             id=txn_id,
#             transaction_id=uuid.uuid4(),
#             flagged_reason="Unusual amount",
#         )
#         db.add(flagged)

#         dispute = PaymentDispute(
#             id=uuid.uuid4(),
#             transaction_id=txn_id,
#             user_id=uuid.uuid4(),
#             dispute_reason="Unauthorized debit",
#         )
#         db.add(dispute)

#         audit = AuditLog(
#             id=uuid.uuid4(),
#             admin_id=uuid.uuid4(),
#             action_type=ActionType.flagged_view,
#             target_id=txn_id,
#             extra_metadata={"note": "Initial flag review"},
#         )
#         db.add(audit)

#         db.commit()
#         print("✅ Seeded DB with flagged txn, dispute, and audit log")


# if __name__ == "__main__":
#     seed()
"""
CLI helper to create schema and insert sample rows.
Run: python -m scripts.seed_db
"""
import uuid
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from src.common.database import init_engine, get_engine, Base
from src.config.settings import settings

# Marketplace models
from src.models.flagged_listings import FlaggedListing
from src.models.disputes import Dispute

# Payments models
from src.models.admin_flags import FlaggedTransaction
from src.models.disputes import PaymentDispute
from src.models.audit_logs import AuditLog, ActionType


# Initialize DB
init_engine(settings.DATABASE_URL)
engine = get_engine()
Base.metadata.create_all(bind=engine)


def seed():
    inspector = inspect(engine)
    with Session(engine) as db:
        # --- Marketplace Sample Data ---
        if "flagged_listings" in inspector.get_table_names():
            if not db.query(FlaggedListing).first():
                db.add_all([
                    FlaggedListing(listing_id=5001, reason="Fake brand item", status="pending"),
                    FlaggedListing(listing_id=5002, reason="Offensive content", status="reviewed"),
                ])
                print("✅ Seeded flagged_listings")

        if "disputes" in inspector.get_table_names():
            if not db.query(Dispute).first():
                db.add_all([
                    Dispute(user_id=2, listing_id=5001, status="open"),
                    Dispute(user_id=3, listing_id=5002, status="resolved"),
                ])
                print("✅ Seeded disputes (Marketplace)")

        # --- Payments Sample Data ---
        if "flagged_transactions" in inspector.get_table_names():
            if not db.query(FlaggedTransaction).first():
                txn_id = uuid.uuid4()
                flagged = FlaggedTransaction(
                    id=txn_id,
                    transaction_id=uuid.uuid4(),
                    flagged_reason="Unusual amount",
                )
                db.add(flagged)
                print("✅ Seeded flagged_transactions")

                dispute = PaymentDispute(
                    id=uuid.uuid4(),
                    transaction_id=txn_id,
                    user_id=uuid.uuid4(),
                    dispute_reason="Unauthorized debit",
                )
                db.add(dispute)
                print("✅ Seeded payment_disputes")

                audit = AuditLog(
                    id=uuid.uuid4(),
                    admin_id=uuid.uuid4(),
                    action_type=ActionType.flagged_view,
                    target_id=txn_id,
                    extra_metadata={"note": "Initial flag review"},
                )
                db.add(audit)
                print("✅ Seeded audit_logs")

        db.commit()
        print("🎉 Database seeding complete")


if __name__ == "__main__":
    seed()
