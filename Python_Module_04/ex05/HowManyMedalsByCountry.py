import numpy as np
import pandas as pd

def how_many_medals_by_country(data, country_name):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby',
                   'Lacrosse', 'Polo']
    data = data.loc[data["Team"] == country_name]
    data1 = data[(data['Team'] == country_name) & (~data['Sport'].isin(team_sports))]
    data2 = data[data['Sport'].isin(team_sports)].drop_duplicates(subset=["Team","NOC","Games","City","Sport","Event","Medal"])
    dictionary = {}
    years = np.unique(data["Year"].array.to_numpy())
    for year in years:
        Gold = len(data1.loc[(data1["Year"] == year) & (data1["Medal"] == "Gold")])
        Gold += len(data2.loc[(data["Year"] == year) & (data2["Medal"] == "Gold")])
        Bronze = len(data1.loc[(data["Year"] == year) & (data1["Medal"] == "Bronze")])
        Bronze += len(data2.loc[(data["Year"] == year) & (data2["Medal"] == "Bronze")])
        Silver = len(data1.loc[(data["Year"] == year) & (data1["Medal"] == "Silver")])
        Silver += len(data2.loc[(data["Year"] == year) & (data2["Medal"] == "Silver")])
        dictionary[year] = {'G': Gold, 'S': Silver, 'B': Bronze}
    print(dictionary)
    return(dictionary)