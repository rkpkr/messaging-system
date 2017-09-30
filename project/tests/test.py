import unittest

from project import app

class ProjectTests(unittest.TestCase):

	# Setup

	def setUp(self):
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		self.app = app.test_client()
		self.assertEquals(app.debug, False)

	def tearDown(self):
		pass

	# Tests

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertIn(b'Testing, testing, 1, 2, 3', response.data)
		self.assertIn(b'Hello, world!', response.data)


if __name__ == '__main__':
	unittest.main()