# DMX Stomps

A modular, extensible DMX foot controller backbone for Raspberry Pi, using a MIDI footswitch (e.g., Ampero Control) as input and DMX output via OLA.

## Features

- MIDI input handling (Ampero Control or similar)
- DMX output via OLA
- Easily extendable for custom mappings, scenes, and effects

## Setup

1. Clone this repo and enter the directory:
   ```sh
   git clone <repo-url>
   cd dmx-stomps
   ```
2. Create and activate the virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running

```sh
python main.py
```

## Roadmap / TODO

- Configurable MIDI-to-DMX mapping
- Scene and preset management
- Web UI for configuration
- Display/LED feedback
- Logging and diagnostics
