import unittest
from maxConv import max_convolution, max_convolution_iterative


class TestMaxConv(unittest.TestCase):

    def test_one_function(self):
        utility_function = [0, 5, 10]
        self.assertListEqual(max_convolution(utility_function), utility_function)
        self.assertListEqual(max_convolution_iterative(utility_function), utility_function)

    def test_two_functions(self):
        first_utility_function = [0, 3, 0, 4, 2]
        second_utility_function = [0, 1, 0, 2, 3]

        expected_function = [0, 3, 4, 4, 5, 6, 6, 7, 5]
        actual_function = max_convolution(first_utility_function, second_utility_function)
        self.assertListEqual(actual_function, expected_function)

        actual_function = max_convolution_iterative(first_utility_function, second_utility_function)        
        self.assertListEqual(actual_function, expected_function)
    def test_three_functions(self):
        first_utility_function = [0, 3, 0, 4, 2]
        second_utility_function = [0, 1, 0, 2, 3]
        third_utility_function = [0, 2, 3, 2, 4]

        expected_function = [0, 3, 5, 6, 7, 7, 8, 9, 9, 10, 10 , 11, 9]
        actual_function = max_convolution(first_utility_function, second_utility_function, third_utility_function)
        self.assertListEqual(actual_function, expected_function)

        actual_function = max_convolution(first_utility_function, second_utility_function, third_utility_function)
        self.assertListEqual(actual_function, expected_function)