minus_inf = float("-infinity")
def adapt(function):
    return [{'val': val, 'conf': [key]} for key, val in enumerate(function)]

def convulate(first_function, second_function):
    conv_function = [{'val': minus_inf, 'conf': []}]*(len(first_function) + len(second_function) - 1)
    for x_i, f_x_i in enumerate(first_function):
        for x_j, f_x_j in enumerate(second_function):
            max_value_candidate = f_x_i['val'] + f_x_j['val']
            if (conv_function[x_i + x_j]['val'] <= max_value_candidate):
                conv_function[x_i + x_j] = {
                    'val': max_value_candidate,
                    'conf': [*f_x_i['conf'], *f_x_j['conf']]}
    return conv_function

def max_convolution(first_function, *other_functions):
    if (len(other_functions) == 0):
        return adapt(first_function)
    else:
        return convulate(adapt(first_function), max_convolution(*other_functions))

def max_convolution_iterative(first_function, *other_functions):
    convulated_function = adapt(first_function)
    for next_function in other_functions:
        convulated_function = convulate(convulated_function, adapt(next_function))
    return convulated_function

def unweight_function(weight, function):
    maxCost = weight*(len(function) - 1)
    return [function[i // weight] if i % weight == 0 else minus_inf for i in range(maxCost + 1)]

def weight_conv_result(weights, result):
    conf = result['conf']
    weighted_conf = [val // weights[key] for key, val in enumerate(conf)]
    return {'val': result['val'], 'conf': weighted_conf}

def max_convolution_weighted(weights, *functions):
    unweighted_functions = [unweight_function(weights[i], function) for i, function in enumerate(functions)]
    convoluted_function = max_convolution(*unweighted_functions)
    weighted_convoluted_function = [ weight_conv_result(weights, result) for key, result in enumerate(convoluted_function)]
    return weighted_convoluted_function