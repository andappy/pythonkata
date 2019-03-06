
import unittest
from helloworldpy import *

class HelloWordPyTest(unittest.TestCase):

	def test_helloworldpy(self):
		self.assertEqual(hello_worldpy(), 'Hello World!')
if __name__ == '__main__':
	unittest.main()
