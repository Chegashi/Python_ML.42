from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# Example 1:
x = [1, 2, 3, 4, 5]
ft_map(lambda dum: dum + 1, x)
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different
print(list(ft_map(lambda t: t + 1, x))) # Output:
# [2, 3, 4, 5, 6]
# Example 2:
ft_filter(lambda dum: not (dum % 2), x)
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different
print(list(ft_filter(lambda dum: not (dum % 2), x))) # Output:
# [2, 4]
# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"