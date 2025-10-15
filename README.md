# 🎛️ DMX Stomps

A complete DMX and MIDI control system with a modern web interface, built with FastAPI backend and React frontend.

## 🏗️ Architecture

```
dmx-stomps/
├── backend/          # FastAPI Python backend
├── frontend/         # React TypeScript frontend
├── start-dev.sh      # Development startup script
└── package.json      # Monorepo management
```

## Prerequisite

* python3
* nodejs LTS

## Install

```
python -m venv ./backend/.venv
chmod +x ./backend/.venv/bin/activate
npm run install:all
```

## 🏃 Run

```
# backend only
source ./backend/.venv/bin/activate
npm run backend:dev
# frontend only
npm run frontend:dev
```