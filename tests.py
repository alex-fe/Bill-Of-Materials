import unittest

import pandas as pd
import pandas.util.testing as pdt

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
        R2,R5,R8
        1.8k
        24"""
        self.correct = [
            'R80b,R80b', '680', '2',
            'R87,R88,R89', '1k', '3',
            'R2,R5,R8', '1.8k', '24'
        ]
        self.df = pd.DataFrame(
            data={
                'Location': ['R80b,R80b', 'R87,R88,R89', 'R2,R5,R8'],
                'Part': ['680', '1k', '1.8k'],
                'Quantity': ['2', '3', '24']
            }
        )

    def test_to_list(self):
        """Test string is properly split into list."""
        result = Formatter.to_list(self.string_as_list)
        self.assertEqual(result, self.correct)

    def test_to_list_as_string(self):
        """Test string is properly split into joined list as type str."""
        correct = ' '.join(self.correct)
        result = Formatter.to_list(self.string_as_list, as_string=True)
        self.assertEqual(result, correct)
        self.assertIsInstance(result, str)

    def test_create_frame(self):
        """Test correct DataFrame is produced."""
        result = Formatter.create_frame(self.string_as_list)
        pdt.assert_frame_equal(result, self.df)


if __name__ == '__main__':
    unittest.main()
