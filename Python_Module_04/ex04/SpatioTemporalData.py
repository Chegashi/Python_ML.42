import numpy as np
import pandas as pd
class SpatioTemporalData:
    def __init__(self, df):
        self.data = df

    def when(self, location):
        return  np.unique(self.data.loc[self.data["City"] == location]["Year"]).tolist()

    def where(self, date):
        return  np.unique(self.data.loc[self.data["Year"] == date]["City"]).tolist()

def main():
    df = pd.read_csv("../athlete_events.csv")
    sp = SpatioTemporalData(df)

    print(sp.where(2000))
    # output is: ['Sydney']

    print(sp.where(1980))
    # output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

    print(sp.when('London'))
    # output is: [2012, 1948, 1908]

if __name__== "__main__":
    main()
