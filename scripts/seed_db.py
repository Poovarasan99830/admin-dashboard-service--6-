import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy.orm import sessionmaker
from src.common.database import init_engine, get_engine, Base
from src.config.settings import settings
from src.models.user import User

def main():
    engine = init_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    if db.query(User).count() == 0:
        users = [
            User(name="John Doe", email="john@example.com"),
            User(name="Alice Smith", email="alice@example.com"),
            User(name="Bob Admin", email="bob@example.com"),
        ]
        db.add_all(users)
        db.commit()
        print("Seeded users into DB ✅")
    else:
        print("Users already exist, skipping seed.")

    db.close()

if __name__ == "__main__":
    main()
