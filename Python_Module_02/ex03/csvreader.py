import os.path
from array import array


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.name = filename
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = None
        self.header = None
        if os.path.isfile(filename):
            self.file_obj = open(filename, 'r')
            lines = self.file_obj.readlines()
            lines = list(map(lambda x: x.replace('\n', ''), lines))
            li = []
            _len = 0
            for i in lines:
                li.append([i])
                if i != lines[0] and _len != len(i.split(sep)):
                    self.file_obj = None
                    return None
                _len = len(list(filter(None, i.split(sep))))
            if header:
                self.header = li[0]
                li = li[1:]
            if (skip_top):
                li = li[skip_top:]
            if (skip_bottom):
                li = li[:-skip_bottom]
            self.data = li if li else None
        else:
            self.file_obj = None

    def __enter__(self):
        if (self.file_obj):
            return self
        pass

    def __exit__(self, type, value, traceback):
        if (self.file_obj):
            return self.file_obj.close()

    def getheader(self):
        return self.header
        # pass

    def getdata(self):
        return self.data
        # pass
