import numpy as np

class SpatioTemporalData:
    def __init__(self, df):
        self.data = df

    def when(self, location):
        return  np.unique(self.data.loc[self.data["City"] == location]["Year"]).tolist()

    def where(self, date):
        return  np.unique(self.data.loc[self.data["Year"] == date]["City"]).tolist()
        