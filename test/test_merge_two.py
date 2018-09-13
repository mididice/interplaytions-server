import pretty_midi
import unittest

class MergeTest(unittest.TestCase):
	def test_read_midi(self):
		midi_data = pretty_midi.PrettyMIDI('180827_01_midi.mid')
		self.assertTrue(midi_data)

	def test_create_object(self):
		cello_c_chord = pretty_midi.PrettyMIDI()
		# Create an Instrument instance for a cello instrument
		cello_program = pretty_midi.instrument_name_to_program('Electric Grand Piano')
		cello = pretty_midi.Instrument(program=cello_program)
		cello_c_chord.instruments.append(cello)
		self.assertEqual(type(cello_c_chord), type(pretty_midi.PrettyMIDI()))

	def test_merge_midi(self):
		egp_chord = pretty_midi.PrettyMIDI()

		egp_program = pretty_midi.instrument_name_to_program('Electric Grand Piano')
		egp = pretty_midi.Instrument(program=egp_program)

		midi_data = pretty_midi.PrettyMIDI('180827_01_midi.mid')
		midi_data2 = pretty_midi.PrettyMIDI('180827_02_midi.mid')

		adding = midi_data.get_end_time()

		for instrument in midi_data.instruments:
			if not instrument.is_drum:
				for note in instrument.notes:
					# print(note.pitch, note.velocity, note.start, note.end)
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start, end=note.end)
					egp.notes.append(note)

		for instrument in midi_data2.instruments:
			if not instrument.is_drum:
				for note in instrument.notes:
					# print(note.pitch, note.velocity, note.start, note.end)
					note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=note.start+adding, end=note.end+adding)
					egp.notes.append(note)

		egp_chord.instruments.append(egp)
		egp_chord.write('egp.mid')

if __name__ == '__main__':
	unittest.main()
