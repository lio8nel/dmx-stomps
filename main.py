from midi.handler import MidiHandler
from dmx.manager import DMXManager

def main():
    print("Starting DMX Stomps controller...")
    midi_handler = MidiHandler()
    try:
        midi_handler.run()
    except KeyboardInterrupt:
        print("Exiting DMX Stomps.")

if __name__ == "__main__":
    main()
