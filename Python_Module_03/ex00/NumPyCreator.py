import numpy as np

class NumPyCreator:
    def __init(self):
        pass

    def from_list(self, lst):
        try:
            if not isinstance(lst, list):
                return None
            if len(lst) > 1:
                for vect in lst:
                    if isinstance(vect, list) and len(lst[0]) != len(vect):
                        return None
            np_arr = np.array(lst)
            return np_arr
        except:
            return None

    def from_tuple(self, tpl):
        try:
            if not isinstance(tpl, tuple) or (isinstance(tpl[0], tuple)):
                return None
            tuple_np = np.array(tpl)
            return tuple_np
        except:
            return None

    def from_iterable(self, itr):
        try:
            if len(itr) > 1:
                for vect in itr:
                    if isinstance(vect, list)\
                        and len(itr[0]) != len(vect):
                        return None
            np_arr = np.array(itr)
            return np_arr
        except:
            return None

    def from_shape(self, *shape, value = 0):
        try:
            if not isinstance(shape, tuple):
                return None
            arr = np.array([value] * shape[0][0] * shape[0][1]).reshape(shape[0][0], shape[0][1])
            for vect in arr:
                if isinstance(vect, list)\
                    and len(arr[0]) != len(vect):
                        return None
            np_arr = np.array(arr)
            return np_arr
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
            arr = np.identity(n)
            return arr
        except:
            return None
