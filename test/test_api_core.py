import requests
import unittest
import shutil
import io


class ApiCoreTest(unittest.TestCase):
	def test_api(self):
		url = 'http://localhost:8000/api/midi/1/2/'
		r = requests.post(url, stream=True)
		if r.status_code == 200:
			with io.open('generate_midi_two.mid', 'wb') as f:
				shutil.copyfileobj(r.raw, f)
			self.assertTrue(r.raw)
		else:
			self.assertTrue(False)
			
	def test_api_1(self):
		url = 'http://localhost:8000/api/midi/2/2/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)


if __name__ == '__main__':
	unittest.main()
