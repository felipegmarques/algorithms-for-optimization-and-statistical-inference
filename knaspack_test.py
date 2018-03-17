import unittest
from knaspack import (
    knaspack, 
)

class TestKnaspack(unittest.TestCase):

    def test_knaspack(self):
        weights = [2, 3, 4]
        values = [2, 4, 7]
        size = 5
        actual_result = knaspack(weights, values, size)
        expected_result = [0, 0, 1]
        self.assertEqual(actual_result, expected_result)
    
