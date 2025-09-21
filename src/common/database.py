# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from typing import Generator
# from src.config.settings import settings

# Base = declarative_base()
# _engine = None
# _SessionLocal = None

# def init_engine(db_url: str):
#     global _engine, _SessionLocal
#     _engine = create_engine(db_url, future=True)
#     _SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)
#     return _engine

# def get_engine():
#     return _engine

# def get_session() -> Generator:
#     """Yield a DB session (use in dependencies)."""
#     global _SessionLocal
#     if _SessionLocal is None:
#         raise RuntimeError("Engine not initialized, call init_engine() first")
#     session = _SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
# from src.config.settings import settings

# engine = create_engine(
#     settings.database_url,
#     pool_pre_ping=True  # helpful with Postgres to avoid stale connections
# )
# SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from src.config.settings import settings
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

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True
)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
