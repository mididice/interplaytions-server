import unittest
import pretty_midi


class ReadMidiTest(unittest.TestCase):
	def test_read_midi(self):
		new_beat = pretty_midi.PrettyMIDI('new1.mid')
		for instrument in new_beat.instruments:
			print(instrument.is_drum)
			for note in instrument.notes:
				print(note.velocity, note.pitch, note.start, note.end)

if __name__ == '__main__':
	unittest.main()
