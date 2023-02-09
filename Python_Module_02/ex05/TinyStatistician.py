 from math import  sqrt

class TinyStatistician():
    def __init__(self, data):
        self.data = data
        self.data_sorted = data.sort()
        self.lent = len(self.data)
    
    def mean(self):
        m = 0
        for items in self.data:
            m += items
        return m / self.lent

    def median(self):
        return self.data_sorted[(self.lent + 1) / 2]

    def quartiles(self, percentile):
        return self.data_sorted[(int(percentile*self.len) / 100)]
    
    def var(self):
        e_caree = 0
        for items in self.data:
            e_caree += items * items
        mean = self.mean()
        return (1 / self.lent) * e_caree - mean * mean

    def std(self):
        m = self.mean()
        s = 0
        for x in self.data:
            s += (x - m) * (x - m)
        return sqrt(s / self.lent)
