def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, "__iter__"):
        return None
    if not hasattr(function_to_apply, "__call__"):
        return None
    return (function_to_apply(iter) for iter in iterable)
