import requests
import unittest

class MergeTest(unittest.TestCase):
	def test_api(self):
		url = 'http://localhost:8000/api/v3/'
		headers = 'Authorization: Token 99919924125885238598329823'
		r = requests.get(url, headers)
		self.assertEqual(r.status_code, 200)

	def test_api2(self):
		url = 'http://localhost:8000/api/test/'
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)		

	def test_combine(self):
		url = 'http://localhost:8000/api/combine/'
		r = requests.post(url)
		print(r.text)
		self.assertEqual(r.status_code, 200)				
if __name__ == '__main__':
	unittest.main()
