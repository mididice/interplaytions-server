import pretty_midi
import os
import uuid
from os import listdir
from os.path import isfile, join
from django.conf import settings


def beat_maker(endtime):
	base_dir = settings.BASE_DIR
	beat_program = pretty_midi.instrument_name_to_program('Synth Drum')
	beat = pretty_midi.Instrument(program=beat_program)
	basic_path = os.path.join(base_dir, 'midibasic')

	basis_beat = pretty_midi.PrettyMIDI(os.path.join(basic_path, 'beat1.mid'))
	for instrument in basis_beat.instruments:
		for note in instrument.notes:
			beat.notes.append(note)
	
	back_beat = pretty_midi.Instrument(program=beat_program)
	beat_length = 0
	# based on midi is 2sec 
	for num in range(0, int(endtime), 2):
		for note in beat.notes:
			note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+beat_length, end=note.end+beat_length)
			back_beat.notes.append(note)
		beat_length += basis_beat.get_end_time()
	return back_beat


def integrate_midi():
	egp_chord = pretty_midi.PrettyMIDI()

	egp_program = pretty_midi.instrument_name_to_program('Lead 8 (bass + lead)')
	egp = pretty_midi.Instrument(program=egp_program)

	media_path = settings.BASE_DIR
	result_path = os.path.join(media_path, 'midiresult')
	generated_path = os.path.join(media_path, 'midifile')
	
	path = generated_path
	midifiles = [file_name for file_name in listdir(path) if isfile(join(path, file_name))]

	midi_notes = []
	adding = 0
	for name in sorted(midifiles):
		if name.endswith('.mid'):
			midi_data = pretty_midi.PrettyMIDI(os.path.join(path, name))
			for instrument in midi_data.instruments:
				for note in instrument.notes:
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+adding, end=note.end+adding)
					midi_notes.append(note)
				
			adding += 4.0

	egp.notes.extend(midi_notes)
	egp_chord.instruments.append(egp)
	egp_chord.instruments.append(beat_maker(adding))

	result_file = str(uuid.uuid4().hex)+".mid"
	egp_chord.write(os.path.join(result_path, result_file))
	return os.path.join(result_path, result_file)


def convert_midi(seq, midi_path):
	midi_chord = pretty_midi.PrettyMIDI()

	midi_program = pretty_midi.instrument_name_to_program('Lead 8 (bass + lead)')
	midi = pretty_midi.Instrument(program=midi_program)

	media_path = settings.BASE_DIR
	result_path = os.path.join(media_path, 'midiresult')
	
	midi_notes = []
	adding = 0
	
	if midi_path.endswith('.mid'):
		midi_data = pretty_midi.PrettyMIDI(midi_path)
		for instrument in midi_data.instruments:
			for note in instrument.notes:
				if note.start > 2.0:
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start-2.0, end=note.end-2.0)
					midi_notes.append(note)
				
	midi.notes.extend(midi_notes)
	midi_chord.instruments.append(midi)
	
	result_file = '{}.mid'.format(seq)
	midi_chord.write(os.path.join(result_path, result_file))
	return os.path.join(result_path, result_file)