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

@app.get("/hello")
async def hello_world():
    """Dummy async route that returns hello world"""
    return {"message": "hello world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
