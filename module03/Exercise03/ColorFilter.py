class ColorFilter:
    def __init__(self):
        pass

    def invert(self, array):
        new_arr = array[:]
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                array[i][j][0] = 256 - array[i][j][1]
                array[i][j][1] = 256 - array[i][j][1]
                array[i][j][1] = 256 - array[i][j][1]
        return new_arr

    def to_blue(self, array):
        new_arr = array[:]
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                array[i][j][2] = 256
        return new_arr

    def to_green(self, array):
        new_arr = array[:]
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                array[i][j][1] = 256
        return new_arr

    def to_red(self, array):
        new_arr = array[:]
        for i in range(0, len(array)):
            for j in range(0, len(array[0])):
                array[i][j][0] = 256
        return new_arr
