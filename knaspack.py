from maxConv import (
    max_convolution_weighted, 
    minus_inf
)

def value_function_builder(weight, value, size):
    return [value*i for i in range((size // weight) + 1)]

def knaspack(weights, values, size):
    functions = [value_function_builder(weights[key], value, size) for key, value in enumerate(values)]
    constraint_helper_function = value_function_builder(1, 0, size)
    functions = [*functions, constraint_helper_function]
    convolutad_function = max_convolution_weighted([*weights, 1], *functions)
    result = convolutad_function[size] 

    return result['conf'][:-1] if result['val'] != minus_inf else []