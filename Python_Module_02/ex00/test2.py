from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

print(list(ft_map(lambda x: x + 2, [])))
#:you should get [].
print(list(ft_map(lambda x: x + 2, [1])))
#: you should get [3].
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
#: you should get [1, 4, 9, 16, 25].
print(list(ft_filter(lambda x: x <= 1, [])))
#: you should get [].
print(ft_reduce((lambda x, y: x + y), [1]))
#: you should get 1.
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))
#: you should get 24. Feel free to realize few more tests.