import unittest
from django.conf import settings

class TokenTest(unittest.TestCase):
	def test_base_dir(self):
		media_path = settings.BASE_DIR
		print(media_path)
if __name__ == '__main__':
	unittest.main()
