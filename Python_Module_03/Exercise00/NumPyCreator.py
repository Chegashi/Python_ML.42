import numpy as np
import random

class NumPyCreator:
    def __init(self):
        pass

    def from_list(self, lst):
        try:
            arr = np.array(lst, dtype=float)
            return arr
        except:
            return None

    def from_tuple(self, tpl):
        try:
            arr = np.array(tpl, dtype='<U1')
            return arr
        except:
            return None

    def from_iterable(self, itr):
        try:
            lst = []
            for items in itr:
                lst.append(items, dtype=type(items))
            return np.array(lst)
        except:
            return None

    def from_shape(self, shape, value = 0):
        try:
            arr = np.array([value] * len(shape), dtype=type(value))
            return arr
        except:
            return None

    def random(self, shape):
        try:
            lst = []
            for i in range(0, len(shape) - 1):
                lst.append(random.randint(0, 1000))
            return np.array(lst, dtype=shape[0])
        except:
            return None

    def identity(self, n):
        try:
            arr = np.identity(n, dtype=type(n))
            return arr
        except:
            return None

npc = NumPyCreator()

# print(npc.from_list([[1,2,3],[6,3,4]]))

# print(npc.from_list([[1,2,3],[6,4]]))

# print(npc.from_tuple(("a", "b", "c")))

# print(npc.from_iterable(range(5)))

# shape=(3,5)

# print(npc.from_shape(shape))

# print(npc.random(shape))

# print(npc.identity(4))
