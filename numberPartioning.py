from maxConv import (
    max_convolution_weighted, 
    minus_inf
)

def produce_number_function(number):
    return [0 if (i == number or i == 0) else minus_inf for i in range(number + 1)]

def number_partioning(numbers):
    cost = sum(numbers)
    weights = [2]*len(numbers)
    functions = [produce_number_function(number) for number in numbers]
    convoluted_function = max_convolution_weighted(weights, *functions)
    solution = convoluted_function[cost]
    return list(filter(lambda x: x != 0, solution['conf'])) if solution['val'] == 0 else []