import unittest
from change import (
    change, 
)

class TestChange(unittest.TestCase):

    def test_change(self):
        coins = [1, 5, 7]
        value = 10
        expected_result = [0, 2, 0]
        actual_result = change(coins, value)
        self.assertListEqual(expected_result, actual_result)
    
