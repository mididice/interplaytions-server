import requests
import unittest
import shutil
import io


class ApiKeyTest(unittest.TestCase):
	def test_api_1(self):
		url = 'http://localhost:8000/api/v2/midi/1/10/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_2(self):
		url = 'http://localhost:8000/api/v2/midi/2/8/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_3(self):
		url = 'http://localhost:8000/api/v2/midi/3/7/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_4(self):
		url = 'http://localhost:8000/api/v2/midi/4/9/'
		r = requests.post(url)
		if r.status_code == 200:
			self.assertTrue(r.text)
		else:
			self.assertTrue(False)

	def test_api_combine(self):
		url = 'http://localhost:8000/api/v2/midi/combine/'
		r = requests.post(url)
		if r.status_code == 200:
			print(r.text)
			self.assertTrue(True)
		else:
			self.assertTrue(False)


if __name__ == '__main__':
	unittest.main()
