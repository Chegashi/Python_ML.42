import numpy as np

def how_many_medals_by_country(data, country_name):
    dic = {}
    data = data.loc[data["Team"] == country_name]
    years = np.unique(data["Year"].array.to_numpy())
    for year in years:
        Gold = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Gold")])
        Bronze = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Bronze")])
        Silver = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Silver")])
        dic[year] = {'G': Gold, 'S': Silver, 'B': Bronze}
    return dic
