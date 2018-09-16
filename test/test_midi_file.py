import unittest
import tensorflow as tf
import io


class MidiFileTest(unittest.TestCase):
	def test_copied_midi(self):
		with tf.gfile.Open('./test.mid', 'rb') as f:
			midi_b = f.read()
		with io.open('copied_midi.mid', 'wb') as f:
			f.write(midi_b)
		with tf.gfile.Open('copied_midi.mid', 'rb') as f:
			copied_b = f.read()
		self.assertEqual(midi_b, copied_b)


if __name__ == '__main__':
	unittest.main()
