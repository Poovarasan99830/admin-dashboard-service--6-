"""
Reset the database: drop all tables, recreate schema, and seed sample data.
Usage:
    python -m scripts.reset_db
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.common.database import init_engine, engine, Base, SessionLocal
from src.config.settings import settings
import scripts.seed_db as seed_script


def reset_db():
    print("⚠️  Dropping all tables...")
    Base.metadata.drop_all(bind=engine)

    print("🛠️  Recreating all tables...")
    Base.metadata.create_all(bind=engine)

    print("🌱 Seeding initial data...")
    seed_script.seed()

    print("✅ Database reset & seeded successfully.")


if __name__ == "__main__":
    # Ensure engine is initialized
    init_engine(settings.database_url)
    reset_db()
