import pretty_midi
import magenta

def midi_json(midi_data):	
	if midi_path.endswith('.mid'):
		primer_sequence = magenta.music.midi_to_sequence_proto(midi_data)
		print(midi_data)

