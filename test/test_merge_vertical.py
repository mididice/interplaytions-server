import pretty_midi
import unittest
import numpy as np

class MergeVerticalTest(unittest.TestCase):
	def test_read_beat(self):
		beat_chord = pretty_midi.PrettyMIDI()
		beat_program = pretty_midi.instrument_name_to_program('Synth Drum')
		beat = pretty_midi.Instrument(program=beat_program)

		basis_beat = pretty_midi.PrettyMIDI('beat1.mid')
		for instrument in basis_beat.instruments:
			print(instrument.is_drum)
			for note in instrument.notes:
				print(note.velocity, note.pitch, note.start, note.end)
				beat.notes.append(note)

		beat_chord.instruments.append(beat)
		adding = 0
		for num in range(0,2):
			for note in beat.notes:
				print(note.start+adding, note.end+adding)
			adding += basis_beat.get_end_time()
		# beat_chord.write('SynthDrum.mid')


	def test_merge_midi(self):
		egp_chord = pretty_midi.PrettyMIDI()
		# egp_program = pretty_midi.instrument_name_to_program('Lead 2 (sawtooth)')
		egp_program = pretty_midi.instrument_name_to_program('Lead 2 (sawtooth)')
		egp = pretty_midi.Instrument(program=egp_program)

		midi_data = pretty_midi.PrettyMIDI('180827_01_midi.mid')
		midi_data2 = pretty_midi.PrettyMIDI('180827_02_midi.mid')

		adding = 0

		for instrument in midi_data.instruments:
			if not instrument.is_drum:
				for note in instrument.notes:
					# print(note.pitch, note.velocity, note.start, note.end)
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start, end=note.end)
					egp.notes.append(note)
		adding += midi_data.get_end_time()
		for instrument in midi_data2.instruments:
			if not instrument.is_drum:
				for note in instrument.notes:
					# print(note.pitch, note.velocity, note.start, note.end)
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+adding, end=note.end+adding)
					egp.notes.append(note)
		adding += midi_data.get_end_time()
		egp_chord.instruments.append(egp)

		beat_program = pretty_midi.instrument_name_to_program('Synth Drum')
		beat = pretty_midi.Instrument(program=beat_program)

		basis_beat = pretty_midi.PrettyMIDI('beat1.mid')
		for instrument in basis_beat.instruments:
			print(instrument.is_drum)
			for note in instrument.notes:
				print(note.velocity, note.pitch, note.start, note.end)
				beat.notes.append(note)
		
		back_beat = pretty_midi.Instrument(program=beat_program)

		beat_length = 0
		for num in range(0, int(adding), 2):
			for note in beat.notes:
				print(note.start+beat_length, note.end+beat_length)
				note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+beat_length, end=note.end+beat_length)
				back_beat.notes.append(note)
			beat_length += basis_beat.get_end_time()
		
		egp_chord.instruments.append(back_beat)
		egp_chord.write('vertical.mid')

if __name__ == '__main__':
	unittest.main()
