import numpy as np
import pandas as pd

def how_many_medals_by_country(data, country_name):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby',
                   'Lacrosse', 'Polo']
    data = data.loc[data["Team"] == country_name]
    data = data[(data['Team'] == country_name) & (~data['Sport'].isin(team_sports))]
    dictionary = {}
    years = np.unique(data["Year"].array.to_numpy())
    for year in years:
        Gold = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Gold")])
        Bronze = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Bronze")])
        Silver = len(data.loc[(data["Year"] == year) & (data["Medal"] == "Silver")])
        dictionary[year] = {'G': Gold, 'S': Silver, 'B': Bronze}
    print(dictionary)