from ft_filter import ft_filter

x = [1, 2, 3, 4, 5]
function = lambda x: x + 1
iterable = [1, 2, 3]

print("# Output:\n<generator object ft_filter at 0x7f709c777d00> # The adress will be different")
print(ft_filter(lambda dum: not (dum % 2), x))
print(filter(lambda dum: not (dum % 2), x))
print("# Output:\n[2, 4]")
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print(list(filter(lambda dum: not (dum % 2), x)))

print(ft_filter(function_to_apply = None, iterable = iterable))
print(filter(function_to_apply = None, iterable = iterable))
print(list(ft_filter(function_to_apply = None, iterable = iterable)))
print(list(filter(function_to_apply = None, iterable = iterable)))
