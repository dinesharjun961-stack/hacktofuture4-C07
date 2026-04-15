# core/database.py
# PURPOSE: Creates the DB engine and session factory
# WHY: Every API route that reads/writes data gets a session from here

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True    # auto-reconnects if DB drops
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# FastAPI routes call this to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db        # hands session to the route
    finally:
        db.close()      # always closes, even on crash
