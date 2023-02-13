from ft_reduce import ft_reduce

function = lambda x: x + 1
iterable = [1, 2, 3]
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"
# ft_reduce(None, iterable = iterable)
# ft_reduce(function, None)
