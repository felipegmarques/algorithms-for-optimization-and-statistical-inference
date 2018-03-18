from maxConv import (
    max_convolution_weighted, 
    minus_inf
)

def coin_function_builder(coin, value):
    return [-i for i in range((value // coin) + 1 )]

def change(coins, value):
    weights = coins
    functions = [coin_function_builder(coin, value) for coin in coins]
    conv_funciton = max_convolution_weighted(weights, *functions)
    result = conv_funciton[value]  
    return result['conf'] if result['val'] != minus_inf else []