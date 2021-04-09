class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.name = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self, data):
        with open(self.name, 'w') as f:
            str1 = self.sep.join([str(elm) for elm in data])
            f.write('\n' + str)
        f.close()

    def __exit__(self):
        return

    def getdata(self):
        data = []
        size = 0
        curent_line = 1
        with open(self.name, 'r') as f:
            while curent_line < self.skip_top:
                f.readlines()
                curent_line += 1
            if self.header :
                header =  f.readlines()
            num_lines = sum(1 for line in open('myfile.txt'))
            for ligne in f:
                if curent_line >= num_lines - self.skip_bottom:
                    break
                curent_line += 1
                ligne_lst = list(ligne.split(self.sep))
                data.append(ligne_lst)
                len_size = len(ligne_lst)
                if not size:
                    size = len_size
                if size == len_size:
                    continue
                else :
                    print("bad csv")
                    f.close
                    return
                


            f.close()
            return data

    def getheader(self):
        if not self.header:
            return ''
        with open(self.name, 'r') as f:
            header =  f.readlines()
            f.close()
            return header