# main.py
# PURPOSE: Entry point — wires all routers together
# WHY: This is what uvicorn runs

from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.events import router as events_router

# Creates all tables in PostgreSQL on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Autonomous Red vs Blue AI Defense System",
    version="1.0.0",
    debug=settings.DEBUG
)

app.include_router(events_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "online", "system": settings.APP_NAME}