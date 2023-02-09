def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) == 1:
        return list_of_inputs[0]
    ret = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for item in list_of_inputs[2:]:
        ret = function_to_apply(ret, item)
    return ret
