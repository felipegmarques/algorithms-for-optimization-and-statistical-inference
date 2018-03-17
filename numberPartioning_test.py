import unittest
from numberPartioning import (
    number_partioning, 
)

class TestNumberPartioning(unittest.TestCase):

    def test_number_partioning(self):
        numbers = [1, 2, 3, 4]
        actual_result = number_partioning(numbers)
        self.assertEqual(2*sum(actual_result), sum(numbers))
        for i in actual_result:
            self.assertTrue(i in numbers)
    
    def test_number_partioning_without_solution(self):
        numbers = [1, 2, 3, 5]
        actual_result = number_partioning(numbers)
        self.assertEqual(len(actual_result), 0)
