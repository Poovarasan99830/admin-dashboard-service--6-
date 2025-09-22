from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
from src.config.settings import settings

engine = None
SessionLocal = None
Base = declarative_base()

def init_engine(database_url: str):
    global engine, SessionLocal
    engine = create_engine(database_url, connect_args={"check_same_thread": False} if database_url.startswith("sqlite") else {})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    if SessionLocal is None:
        init_engine(settings.DATABASE_URL)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
