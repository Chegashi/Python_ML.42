from math import  sqrt

class TinyStatistician():
    def __init__(self):
        pass

    def mean(self, data):
        if len(data) == 0:
            return None
        m = 0
        for items in data:
            m += items
        return float(m / len(data))

    def median(self, data):
        data.sort()
        if len(data) == 0:
            return None
        return float(data[len(data)//2])

    def quartile(self, data):
        data.sort()
        if len(data) == 0:
            return None
        return [float(data[len(data)//4]), float(data[int(len(data)*(3/4))])]
    
    def var(self, data):
        if len(data) == 0:
            return None
        sigma = 0
        _mean = self.mean(data)
        for items in data:
            sigma += (items - _mean) * (items - _mean)
        return sigma / len(data)

    def std(self, data):
        if len(data) == 0:
            return None
        return sqrt(self.var(data))

