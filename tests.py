import unittest

from utils import Formatter

# utils
class TestFormatter(unittest.TestCase):

    def setUp(self):
        self.string_as_list = """R80b,R80b
        680
        2
        R87,R88,R89
        1k
        3
        R2,R5,R8,R11,R14,R17,R20,R23,R26,R29,R32,R35,R38,R41,R44
        1.8k
        24"""
        self.correct = [
            'R80b,R80b', '680', '2',
            'R87,R88,R89', '1k', '3',
            'R2,R5,R8,R11,R14,R17,R20,R23,R26,R29,R32,R35,R38,R41,R44',
            '1.8k', '24'
        ]

    def test_to_list(self):
        """Test string is properly split into list."""
        result = Formatter.to_list(self.string_as_list)
        self.assertEquals(result, self.correct)

    def test_to_list_as_string(self):
        """Test string is properly split into joined list as type str."""
        correct = ' '.join(self.correct)
        result = Formatter.to_list(self.string_as_list, as_string=True)
        self.assertEquals(result, correct)
        self.assertIsInstance(result, str)

    def test_create_frame(self):
        result = Formatter.create_frame(self.string_as_list)


if __name__ == '__main__':
    unittest.main()
