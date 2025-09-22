# Run: python scripts/seed_db.py
from src.common.database import init_engine, engine, Base, SessionLocal
from src.config.settings import settings
from src.models.user import User

def main():
    init_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    # avoid duplicates
    if db.query(User).count() == 0:
        users = [
            User(name="John Doe", email="john@example.com"),
            User(name="Alice Smith", email="alice@example.com"),
            User(name="Bob Admin", email="bob@example.com"),
        ]
        db.add_all(users)
        db.commit()
    db.close()
    print("seeded DB")

if __name__ == "__main__":
    main()
