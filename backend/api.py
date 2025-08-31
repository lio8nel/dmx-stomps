from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def get_stomps():
    return {
        "stomps": [
            { "id": "s-1", "name": "Stomp 1", "state": "off" },
            { "id": "s-2", "name": "Stomp 2", "state": "off" }
        ]
    }

@app.put("/stomps/{id}")
async def toggle_stomps(id: str):
    return { "id": id,"state": "on" }
