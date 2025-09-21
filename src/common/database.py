from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

Base = declarative_base()
_engine = None
_SessionLocal = None

def init_engine(db_url: str):
    global _engine, _SessionLocal
    _engine = create_engine(db_url, future=True)
    _SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)
    return _engine

def get_engine():
    return _engine

def get_session() -> Generator:
    """Yield a DB session (use in dependencies)."""
    global _SessionLocal
    if _SessionLocal is None:
        raise RuntimeError("Engine not initialized, call init_engine() first")
    session = _SessionLocal()
    try:
        yield session
    finally:
        session.close()
