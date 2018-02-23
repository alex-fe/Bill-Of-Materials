import unittest

from utils import Formatter

# utils
class Formatter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('tester.txt', 'r') as myfile:
            cls.data = myfile.read()

    def test_remove_whitespace(self):
        pass


if __name__ == '__main__':
    unittest.main()
