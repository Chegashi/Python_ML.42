import numpy as np

def howManyMedals(data, name):
    dic = {}
    data = data.loc[data["Name"] == name]
    years = np.unique(data["Year"].array.to_numpy())
    for year in years:
        Gold = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Gold")])
        Bronze = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Bronze")])
        Silver = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Silver")])
        dic[year] = {'G': Gold, 'S': Silver, 'B': Bronze}
    return dic
