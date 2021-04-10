import numpy as np
import random

class NumPyCreator:
    def __init(self):
        pass

    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        lst = []
        for items in itr:
            lst.append(items)
        return np.array(lst)

    def from_shape(self, shape, value = 0):
        return np.array([value] * len(shape))

    def random(self, shape):
        lst = []
        for i in range(0, len(shape) - 1):
            lst.append(random.randint(0, 1000))
        return np.array(lst)

    def identity(self, n):
        return np.identity(n)


npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))

print(npc.from_tuple(("a", "b", "c")))

print(npc.from_iterable(range(5)))

shape=(3,5)

print(npc.from_shape(shape))

print(npc.random(shape))

print(npc.identity(4))
