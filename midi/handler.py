import sys
import mido

class MidiHandler:
    def run(self):
        print("[MIDI] Listening for MIDI events...")
        # TODO: Replace with actual MIDI event loop
        with mido.open_input("MidiKeys") as port:
            print(f'Using {port}')
            print('Waiting for messages...')
            for message in port:
                print(f'Received {message}')
                sys.stdout.flush()
