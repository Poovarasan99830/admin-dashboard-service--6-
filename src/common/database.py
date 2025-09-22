from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

# Base class for all models
Base = declarative_base()

# Global engine/session objects
_engine = None
_SessionLocal = None


def init_engine(db_url: str):
    """
    Initialize the SQLAlchemy engine and sessionmaker.
    Call this once on app startup.
    """
    global _engine, _SessionLocal
    _engine = create_engine(db_url, future=True, pool_pre_ping=True)
    _SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)
    return _engine


def get_engine():
    """Return the global SQLAlchemy engine (or None if not initialized)."""
    return _engine


def get_session() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI routes.
    Yields a session that is closed after use.
    """
    global _SessionLocal
    if _SessionLocal is None:
        raise RuntimeError("Engine not initialized. Call init_engine() first.")
    session: Session = _SessionLocal()
    try:
        yield session
    finally:
        session.close()
