from ft_map import ft_map

x = [1, 2, 3, 4, 5]
print("# Output: \n<generator object ft_map at 0x7f708faab7b0> # The adress will be different")
print(ft_map(lambda dum: dum + 1, x))
# print("# Output: [2, 3, 4, 5, 6]")
print(list(map(lambda dum: dum + 1, x)))
print(list(ft_map(lambda t: t + 1, x)))

function = lambda x: x + 1
iterable = [1, 2, 3]
# ft_map(function_to_apply = None, iterable = iterable)
# map(function_to_apply = None, iterable = iterable)
# print("Should print \"< generator object at hexa_adress>\"")
# list(ft_map(function_to_apply = None, iterable = iterable))
# print("You should get an Error")
