class Vector():
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0]))

    def dot(self, a):
        d = 0
        if isinstance(a, type(self)):
            if a.shape == self.shape:
                for colomn in range(self.shape[0]):
                    for row in range(self.shape[1]):
                        d += self.values[colomn][row] * a.values[colomn][row]
            return(d)
        else:
            raise TabError("ERROR only integrers and list with identic lenght")

    def T(self):
        li = []
        for colomn in range(self.shape[1]):
            r = []
            for row in range(self.shape[0]):
                r.append(self.values[row][colomn])
            li.append(r)
        return Vector(li)

    def __str__(self):
        return ("(Vector {})".format(self.values))

    def __add__(self, a):
        li = []
        if isinstance(a, type(self)):
            if a.shape == self.shape:
                for c in range(self.shape[0]):
                    r = []
                    for row in range(self.shape[1]):
                        r.append(self.values[c][row] + a.values[c][row])
                    li.append(r)
        else:
            raise TabError("ERROR only for 2 vectors of the same shape,")
        return li

    def __radd__(self, a):
        return self.__add__(a)

    def __mul__(self, a):
        li = []
        if (isinstance(a, int) or isinstance(a, float)):
            for colomn in self.values:
                r = []
                for row in colomn:
                    r.append(row * a)
                li.append(r)
        else:
            self.__rmul__(a)
        return(li)

    def __rmul__(self, a):
        raise TabError("nly scalars (to perform multiplication of \
      Vector by a scalar).")

    def __sub__(self, a):
        li = []
        if isinstance(a, type(self)):
            if a.shape == self.shape:
                for c in range(self.shape[0]):
                    r = []
                    for row in range(self.shape[1]):
                        r.append(self.values[c][row] - a.values[c][row])
                    li.append(r)
        else:
            raise TabError("ERROR only for 2 vectors of the same shape,")
        return li

    def __rsub__(self, a):
        return self.__sub__(a)

    def __truediv__(self, a):
        if (isinstance(a, int) or isinstance(a, float)):
            if (not a):
                raise TabError("ZeroDivisionError: division by zero")
            li = []
            if isinstance(a, type(self)):
                if a.shape == self.shape:
                    for colomn in range(self.shape[0]):
                        r = []
                        for row in range(self.shape[1]):
                            r.append(self.values[colomn][row] / a)
                        li.append(r)
        else:
            self.__rtruediv__(a)
        return li

    def __rtruediv__(self, a):
        raise TabError('# rtruediv : raises an NotImplementedError with the \
      message "Division of a scalar by a Vector is not defined here."')

    def __repr__(self):
        return ("(Vector shape : {}\n\
            Vector valeus : {})".format(self.shape, self.values))
