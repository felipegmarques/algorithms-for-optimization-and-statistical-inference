minus_inf = float("-infinity")
def convulate(first_function, second_function):
    conv_function = [minus_inf]*(len(first_function) + len(second_function) - 1)
    for x_i, f_x_i in enumerate(first_function):
        for x_j, f_x_j in enumerate(second_function):
            conv_function[x_i + x_j] = max(conv_function[x_i + x_j], f_x_j + f_x_i)
    return conv_function

def max_convolution(first_function, *other_functions):
    if (len(other_functions) == 0):
        return first_function
    else:
        return convulate(first_function, max_convolution(*other_functions))

def max_convolution_iterative(first_function, *other_functions):
    convulated_function = first_function
    for next_function in other_functions:
        convulated_function = convulate(next_function, convulated_function)
    return convulated_function