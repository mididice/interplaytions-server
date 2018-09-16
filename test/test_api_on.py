import requests
import unittest
import tensorflow as tf
import os, os.path, sys
import io
import shutil


class ApiTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(ApiTest, self).__init__(*args, **kwargs)
		sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

	def test_api(self):
		url = 'http://localhost:8000/api/v3/'
		headers = 'Authorization: Token 99919924125885238598329823'
		r = requests.get(url, headers)
		self.assertEqual(r.status_code, 403)

	def test_api2(self):
		url = 'http://localhost:8000/api/test/'
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)		

	def test_combine(self):
		url = 'http://localhost:8000/api/combine/'
		r = requests.post(url)
		print(bytearray(r.text,'utf-8'))
		self.assertEqual(r.status_code, 200)

	def test_request_midi(self):
		url = 'http://localhost:8000/api/v2/'
		headers = {"content-type":"audio/midi"}
		with tf.gfile.Open('./test.mid', 'rb') as f:
			midi_str = f.read()

		r = requests.post(url, data=midi_str, headers=headers, stream=True)
		if r.status_code == 200:
			with io.open('generated_test_midi.mid', 'wb') as f:
				shutil.copyfileobj(r.raw, f)
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
	unittest.main()
