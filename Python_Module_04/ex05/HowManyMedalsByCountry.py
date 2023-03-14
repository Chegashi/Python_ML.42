import numpy as np
import pandas as pd

def how_many_medals_by_country(data, country_name):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby',
                   'Lacrosse', 'Polo']
    data = data.loc[data["Team"] == country_name]
    data2 = data[data['Sport'].isin(team_sports)].drop_duplicates(["Team","NOC","Games","City","Sport","Event","Medal"])
    dictionary = {}
    years = np.unique(data["Year"].array.to_numpy())
    data = pd.concat([data[~data['Sport'].isin(team_sports)], data2])
    for year in years:
        Gold = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Gold")])
        Bronze = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Bronze")])
        Silver = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Silver")])
        dictionary[year] = {'G': Gold, 'S': Silver, 'B': Bronze}
    return(dictionary)