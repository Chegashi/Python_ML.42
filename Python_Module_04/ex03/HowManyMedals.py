import numpy as np
from FileLoader import FileLoader

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

def main():
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    print(howManyMedals(data, 'Gary Abraham'))
    #  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

    print(howManyMedals(data, 'Yekaterina Konstantinovna Abramova'))
    #  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

    print(howManyMedals(data, 'Kristin Otto'))
    #  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"

if __name__=="__main__":
    main()