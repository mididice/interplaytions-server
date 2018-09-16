import requests
import unittest
import shutil
import io


class ApiCoreTest(unittest.TestCase):
	def test_api(self):
		url = 'http://localhost:8000/api/midi/3'
		r = requests.post(url, stream=True)
		if r.status_code == 200:
			with io.open('generate_midi_one.mid', 'wb') as f:
				shutil.copyfileobj(r.raw, f)
			self.assertTrue(r.raw)
		else:
			self.assertTrue(False)


if __name__ == '__main__':
	unittest.main()
