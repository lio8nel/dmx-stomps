from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core import Stomp, StompRepository
from core.toggle_stomp import ToggleStompCommand
from infrastructure import InMemoryStompRepository
from pydantic import BaseModel
from typing import Literal

# Create FastAPI app instance
app = FastAPI(
    title="DMX Stomps API",
    description="REST API for DMX and MIDI control",
    version="1.0.0"
)

# Add CORS middleware for web frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "DMX Stomps API is running"}

@app.get("/stomps")
async def get_stomps(stomp_repository: StompRepository = Depends(InMemoryStompRepository)):
    stomps = stomp_repository.get_stomps()
    return {
        "stomps": [
            { "id": s.id, "name": s.name, "state": s.state } for s in stomps
        ]
    }

class StompState(BaseModel):
    state: Literal["on", "off"]

@app.put("/stomps/{id}")
async def toggle_stomps(
    id: str,
    payload: StompState,
    stomp_repository: StompRepository = Depends(InMemoryStompRepository)
):
    command = ToggleStompCommand(stomp_repository)
    commandResult = command.execute(id, payload.state)
    if commandResult is None:
        raise HTTPException(status_code=404, detail="Stomp not found")
    return { "id": id, "state": commandResult.state }
