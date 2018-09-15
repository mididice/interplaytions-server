import pretty_midi
import os
from os import listdir
from os.path import isfile, join
from django.conf import settings


class Integration():
	def united_midi(self, dir_name):
		egp_chord = pretty_midi.PrettyMIDI()

		egp_program = pretty_midi.instrument_name_to_program('Electric Grand Piano')
		egp = pretty_midi.Instrument(program=egp_program)

		media_path = settings.BASE_DIR
		mypath = '1451390768'
		result_path = os.path.join(media_path, 'midiresult')
		media_path = os.path.join(media_path, 'midifile')
		
		path = os.path.join(media_path, mypath)
		midifiles = [file_name for file_name in listdir(path) if isfile(join(path, file_name))]

		midi_notes = []
		adding = 0
		for name in sorted(midifiles):
			print(name)
			if name.endswith('.mid'):
				midi_data = pretty_midi.PrettyMIDI(os.path.join(path, name))
			for instrument in midi_data.instruments:
				if not instrument.is_drum:
					for note in instrument.notes:
						note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+adding, end=note.end+adding)
						midi_notes.append(note)
			adding = midi_data.get_end_time()

		egp.notes.extend(midi_notes)
		egp_chord.instruments.append(egp)
		result_file = mypath+'.mid'
		egp_chord.write(os.path.join(result_path, result_file))
		return os.path.join(result_path, result_file)
