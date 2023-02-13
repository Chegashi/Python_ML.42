def ft_reduce(function_to_apply, list_of_inputs):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if len(list_of_inputs) == 1:
        return list_of_inputs[0]
    ret = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for item in list_of_inputs[2:]:
        ret = function_to_apply(ret, item)
    return ret
