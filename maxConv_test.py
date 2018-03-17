import unittest
from maxConv import (max_convolution_weighted, 
    max_convolution, 
    max_convolution_iterative,
    unweight_function,
    weight_conv_result,
    minus_inf)

class TestCaseConv(unittest.TestCase):
    def assertConvolutionFunction(self, function, expected_values, convoluted_functions, weights = []):
        self.assertLengthEqualTo(function, len(expected_values))
        if (len(weights) == 0):
            weights = [1]*len(convoluted_functions)

        for cost in range(len(function)):
            actual_value = function[cost]['val']
            expected_value = expected_values[cost]
            try:
                self.assertEqual(actual_value, expected_value)
            except AssertionError:
                raise AssertionErrorForCost(cost, 'values differ: %d != %d' % (actual_value, expected_value))

            conf = function[cost]['conf']
            try:
                self.assertLengthEqualTo(conf, len(convoluted_functions))
            except AssertionError:
                raise AssertionErrorForCost(cost, "configuration doesn't have expected length %d" % (len(convoluted_functions)))
            
            conf_cost = sum([weights[function_index]*val for function_index, val in enumerate(conf)]) 
            try:
                self.assertEqual(conf_cost, cost)
            except AssertionError:
                raise AssertionErrorForCost(cost, "configuration cost differ: %d != %d" % (conf_cost, cost))

            actual_conf_value = sum([ convoluted_functions[key][val] for key, val in enumerate(conf)])
            try:
                self.assertEqual(actual_conf_value, expected_value)
            except AssertionError:
                raise AssertionErrorForCost(cost, "configuration value differ: %d != %d" % (actual_conf_value, expected_value))

    def assertLengthEqualTo(self, array, length):
        try:
            self.assertEqual(len(array), length)
        except AssertionError:
            raise AssertionError("doesn't have expected length %d", length)


class TestMaxConv(TestCaseConv):

    def test_one_function(self):
        utility_function = [0, 5, 10]
        self.assertConvolutionFunction(max_convolution(utility_function), utility_function, [utility_function])
        self.assertConvolutionFunction(max_convolution_iterative(utility_function), 
            utility_function, 
            [utility_function])

    def test_two_functions(self):
        first_utility_function = [0, 3, 0, 4, 2]
        second_utility_function = [0, 1, 0, 2, 3]

        functions = [first_utility_function, second_utility_function]
        expected_values = [0, 3, 4, 4, 5, 6, 6, 7, 5]

        actual_function = max_convolution(*functions)
        self.assertConvolutionFunction(actual_function, expected_values, functions)
        actual_function = max_convolution_iterative(*functions)
        self.assertConvolutionFunction(actual_function, expected_values, functions)

    def test_three_functions(self):
        first_utility_function = [0, 3, 0, 4, 2]
        second_utility_function = [0, 1, 0, 2, 3]
        third_utility_function = [0, 2, 3, 2, 4]

        functions = [first_utility_function, second_utility_function, third_utility_function]
        expected_values = [0, 3, 5, 6, 7, 7, 8, 9, 9, 10, 10 , 11, 9]

        actual_function = max_convolution(*functions)
        self.assertConvolutionFunction(actual_function, expected_values, functions)

        actual_function = max_convolution_iterative(*functions)
        self.assertConvolutionFunction(actual_function, expected_values, functions)

def AssertionErrorForCost(cost, msg):
    return AssertionError("For cost = %d, %s" % (cost, msg))


class TestMaxConvWeighted(TestCaseConv):

    def test_unweight_function(self):
        function = [0, 1, 2, 3, 4]
        weight = 2
        expected_unweighted_function = [0, minus_inf, 1, minus_inf, 2, minus_inf, 3, minus_inf, 4]
        actual_unweighted_function = unweight_function(weight, function)
        self.assertListEqual(actual_unweighted_function, expected_unweighted_function)
    
    def test_weight_conv_result(self):
        weights = [2, 1]
        unweighted_result = {'val': 4, 'conf': [2, 1]}
        expected_result = {'val': 4, 'conf': [1, 1]}
        actual_result = weight_conv_result(weights, unweighted_result)
        self.assertDictEqual(actual_result, expected_result)

    def test_weighted_max_convolution(self):
        first_function = [0, 1, 2]
        second_function = [0, 4, 3]
        weights = [2, 1]

        functions = [first_function, second_function]
        expected_values = [0, 4, 3, 5, 4, 6, 5]
        actual_function = max_convolution_weighted(weights, *functions)
        self.assertConvolutionFunction(actual_function, expected_values, functions, weights)
