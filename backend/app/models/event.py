# models/event.py
# PURPOSE: Defines the "events" table in PostgreSQL
# WHY: Every Red agent attack & Blue agent response is logged as an Event

from sqlalchemy import Column, Integer, String, DateTime, Text, Enum
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class AgentType(str, enum.Enum):
    RED = "red"
    BLUE = "blue"

class EventStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    agent_type = Column(Enum(AgentType), nullable=False)   # red or blue
    action = Column(String(255), nullable=False)            # e.g. "nmap_scan"
    target = Column(String(255), nullable=True)             # e.g. "192.168.1.1"
    result = Column(Text, nullable=True)                    # scan output
    status = Column(Enum(EventStatus), default=EventStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
