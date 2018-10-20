import requests
import unittest
import shutil
import io
import pretty_midi

class ApiAnalyzeTest(unittest.TestCase):
	# def test_api(self):
	# 	url = 'http://localhost:8000/api/v2/midi/analyze/'
	# 	with io.open('generate_midi_two.mid', 'wb') as f:
	# 		data = f.write()
	# 	r = requests.post(url, stream=True, data = data)
	# 	if r.status_code == 200:
	# 		self.assertTrue(r.text)
	# 	else:
	# 		self.assertTrue(False)
	def test_analyze(self):
		result = []
		
		midi_data = pretty_midi.PrettyMIDI('180827_01_midi.mid')
		for instrument in midi_data.instruments:
			for note in instrument.notes:
				notes = {}
				notes['start'] = note.start
				notes['end'] = note.end
				notes['pitch'] = note.pitch
				notes['velocity'] = note.velocity
				result.append(notes)

		print(result)

if __name__ == '__main__':
	unittest.main()
