import requests
import unittest
import shutil
import io


class ApiKeyTest(unittest.TestCase):
	def test_api_1(self):
		url = 'http://localhost:8000/api/midi/1/10/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_2(self):
		url = 'http://localhost:8000/api/midi/2/8/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_3(self):
		url = 'http://localhost:8000/api/midi/3/7/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_4(self):
		url = 'http://localhost:8000/api/midi/4/9/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_combine(self):
		url = 'http://localhost:8000/api/midi/combine/'
		r = requests.post(url, stream=True)
		if r.status_code == 200:
			with io.open('generate_midi_1007.mid', 'wb') as f:
				shutil.copyfileobj(r.raw, f)
			self.assertTrue(f)
		else:
			self.assertTrue(False)


if __name__ == '__main__':
	unittest.main()
