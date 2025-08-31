#!/bin/bash

# DMX Stomps Development Startup Script
# This script starts both the backend API and frontend React app

echo "🎛️  Starting DMX Stomps Development Environment..."
echo ""

# Function to cleanup background processes on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down development servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Start backend server
echo "🚀 Starting Backend API server..."
cd backend
python -m uvicorn backend.api:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 2

# Start frontend server
echo "🎨 Starting Frontend React app..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Development servers started!"
echo "📡 Backend API: http://localhost:8000"
echo "🎨 Frontend App: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Wait for both processes
wait
