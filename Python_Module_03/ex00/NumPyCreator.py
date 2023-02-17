import numpy as np

class NumPyCreator:
    def __init(self):
        pass

    def from_list(self, lst):
        try:
            return np.array(lst, dtype='<U21')
        except:
            return None

    def from_tuple(self, tpl):
        try:
            if not isinstance(tpl, tuple):
                return None
            arr = np.array(tpl, dtype='<U1')
            return arr
        except:
            return None

    def from_iterable(self, itr):
        try:
            lst = []
            for items in itr:
                lst.append(items)
            arr = np.array(lst)
            return arr
        except:
            return None

    def from_shape(self, *shape, value = 0):
        try:
            if not isinstance(shape, tuple):
                return None
            arr = np.array([value] * shape[0][0] * shape[0][1], dtype='f')
            arr = arr.reshape(shape[0][0], shape[0][1])
            return arr
        except:
            return None

    def random(self, *shape):
        try:
            lst = []
            for i in range(shape[0][0] * shape[0][1]):
                lst.append(np.random.rand())
            arr = np.array(lst).reshape(shape[0][0], shape[0][1])
            return arr
        except:
            return None

    def identity(self, n):
        try:
            arr = np.identity(n, dtype=type(n))
            return arr
        except:
            return None

# npc = NumPyCreator()

# print(npc.from_list("toto"))
# print("Shoud Output:\nNone\n\n")

# print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
# print("Shoud Output:\nNone\n\n")

# print(npc.from_tuple(3.2))
# print("Shoud Output:\nNone\n\n")

# print(npc.from_tuple(((1,5,8),(7,5))))
# print("Shoud Output:\nNone\n\n")

# print(npc.from_shape((-1, -1)))
# print("Shoud Output:\nNone\n\n")

# print(npc.identity(-1))
# print("Shoud Output:\nNone\n\n")
