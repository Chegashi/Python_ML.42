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
        if isinstance(n, int):
            if n > 0:
                print(df.head(n))
            if n < 0:
                print(df.tail(-1*n))
    
def main():
    f = FileLoader()
    df = f.load("../athlete_events.csv")
    # Should output (approximately) :
        # (271116, 15) 
    f.display(df, 3)
    # # Should Output
    #     #    ID                 Name Sex   Age  Height  Weight     Team  NOC        Games  Year  Season       City       Sport                         Event Medal
    #     # 0   1            A Dijiang   M  24.0   180.0    80.0    China  CHN  1992 Summer  1992  Summer  Barcelona  Basketball   Basketball Men's Basketball   NaN
    #     # 1   2             A Lamusi   M  23.0   170.0    60.0    China  CHN  2012 Summer  2012  Summer     London        Judo  Judo Men's Extra-Lightweight   NaN
    #     # 2   3  Gunnar Nielsen Aaby   M  24.0     NaN     NaN  Denmark  DEN  1920 Summer  1920  Summer  Antwerpen    Football       Football Men's Football   NaN
    f.display(df, -3)
    # # Should output:
    #     # ID                Name Sex   Age  Height  Weight    Team  NOC        Games  Year  Season            City        Sport                               Event Medal
    #     # 271113  135570            Piotr ya   M  27.0   176.0    59.0  Poland  POL  2014 Winter  2014  Winter           Sochi  Ski Jumping  Ski Jumping Men's Large Hill, Team   NaN
    #     # 271114  135571  Tomasz Ireneusz ya   M  30.0   185.0    96.0  Poland  POL  1998 Winter  1998  Winter          Nagano    Bobsleigh                Bobsleigh Men's Four   NaN
    #     # 271115  135571  Tomasz Ireneusz ya   M  34.0   185.0    96.0  Poland  POL  2002 Winter  2002  Winter  Salt Lake City    Bobsleigh                Bobsleigh Men's Four   NaN
    f.display(df, 0)
    # # should display Nothing or the Header (column names of the dataframe)
    f.display(df, "lol")
    #shouldnt crash


if __name__ == "__main__":
    main()

