minus_inf = float("-infinity")
def max_convolution(first_function, *other_functions):
    if (len(other_functions) == 0):
        return first_function
    else:
        rest_covolution = max_convolution(*other_functions)
        result_convolution = [minus_inf]*(len(first_function) + len(rest_covolution) - 1)
        for first in range(len(first_function)):
            for second in range(len(rest_covolution)):
                result_convolution[first + second] = max(result_convolution[first + second], first_function[first] + rest_covolution[second])

        return result_convolution

def max_convolution_iterative(*functions):
    conv_function = functions[0];
    for fun  in functions[1:]:
        old_conv_function = conv_function
        conv_function = [minus_inf]*(len(fun) + len(old_conv_function) - 1)
        for x_i, f_x_i in enumerate(fun):
            for x_j, f_x_j in enumerate(old_conv_function):
                conv_function[x_i + x_j] = max(conv_function[x_i + x_j], f_x_j + f_x_i)
    return conv_function