# schemas/event.py
# PURPOSE: Defines what the API accepts (input) and returns (output)
# WHY: FastAPI validates every request against these — wrong data = auto 422 error

from pydantic import BaseModel
from datetime import datetime
from app.models.event import AgentType, EventStatus
from typing import Optional

class EventCreate(BaseModel):
    agent_type: AgentType
    action: str
    target: Optional[str] = None

class EventResponse(EventCreate):
    id: int
    result: Optional[str] = None
    status: EventStatus
    created_at: datetime

    class Config:
        from_attributes = True
