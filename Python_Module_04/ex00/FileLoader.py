#!/usr/bin/env python3.7

import pandas as pd

class FileLoader:
    _df = None
    numberRaw = 0
    numberComumn = 0

    def load(self, path):
        self._df = pd.read_csv(path)
        numberRaw, numberComumn = self._df.shape
        print("Loading dataset of dimensions {} x {}".format(numberRaw, numberComumn))
        return self._df


    def display(self, df, n):
        if not isinstance(n, int):
            return ""
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-1*n))