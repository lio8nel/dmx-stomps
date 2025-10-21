# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DMX Stomps is a DMX and MIDI control system with a web interface. It allows users to toggle "stomps" (lighting effects) via a React frontend that communicates with a FastAPI backend, which controls DMX lighting hardware via OLA (Open Lighting Architecture).

## Development Commands

### Installation
```bash
# Create Python virtual environment
python -m venv ./backend/.venv
chmod +x ./backend/.venv/bin/activate

# Install all dependencies
npm run dev:install
```

### Running the Application
```bash
# Activate Python virtual environment first
source ./backend/.venv/bin/activate

# Run backend only (FastAPI on port 8000)
npm run backend:dev

# Run frontend only (Vite dev server)
npm run frontend:dev
```

### Testing
```bash
# Backend tests (from root or with venv activated)
npm run backend:test
# Or: cd backend && pytest -q

# Frontend tests
cd frontend && npm run test
```

### Building
```bash
# Frontend production build
npm run frontend:build

# Preview production build
npm run frontend:preview
```

## Architecture

This is a **monorepo** with two main components:

### Backend (Python/FastAPI)
- **Framework**: FastAPI with uvicorn
- **Architecture**: Clean Architecture / DDD-inspired
  - `domain/`: Core business entities (`Stomp`, `StompRepository` interface)
  - `infrastructure/`: Concrete implementations (`InMemoryStompRepository`, `DmxDeamon`)
  - `commands/`: Command pattern for operations (`ToggleStompCommand`)
  - `commands/handlers/`: Command handlers execute business logic
  - `dmx/`: DMX hardware communication via OLA
  - `midi/`: MIDI input handling via mido/python-rtmidi
  - `api.py`: FastAPI app with REST endpoints and dependency injection

- **Key Patterns**:
  - Repository pattern for data access
  - Command/Handler pattern for operations
  - Singleton pattern for `DmxDeamon`
  - FastAPI `Depends()` for dependency injection

- **API Endpoints**:
  - `GET /stomps` - List all stomps
  - `PUT /stomps/{id}` - Toggle stomp state (on/off)
  - `POST /deamon/start` - Start DMX daemon
  - `POST /deamon/stop` - Stop DMX daemon

### Frontend (React/TypeScript)
- **Framework**: React 19 with TypeScript, Vite
- **State Management**: TanStack Query (React Query) for server state
- **Structure**:
  - `src/api/stomps.ts`: API client functions
  - `src/App.tsx`: Main component with stomp list and toggle buttons
  - Tests use Vitest + React Testing Library

## Testing Guidelines

When writing tests, follow these project-specific conventions:
- Use `// Arrange`, `// Act`, `// Assert` comments to structure tests
- Use BDD style when possible
- Don't over-factor tests unless explicitly requested
- Name the system under test `sut`
- **Important**: When writing tests, don't implement the actual code unless asked

## Code Style

- **No comments**: Code should be self-explanatory
- **Short functions**: Avoid long functions
- **Low cyclomatic complexity**: Keep logic simple and readable
- **No emojis** in code unless explicitly requested

## Important Notes

- The backend uses a **singleton pattern** for `DmxDeamon` to ensure only one instance manages DMX hardware
- CORS is currently configured with `allow_origins=["*"]` - configure properly for production
- The `InMemoryStompRepository` is the current implementation; production may need persistent storage
- MIDI handler (`midi/handler.py`) is partially implemented and hardcoded to "MidiKeys" port
