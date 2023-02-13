def youngestfellah(data, year):
    # return(data.sort_values(["Age"], ascending=True).iloc[4:0])
    # data_M = data.loc[data["Year"] == year & data["Sex"] == "M"]
    # data_F = data.loc[data["Year"] == year & data["Sex"] == "F"]  
    data_F = data.loc[(data["Year"] == year) & (data["Sex"] == "F")]["Age"]
    # youngest = data.loc[data["Age"], "year" = year]
    return(data_F.max(["Age"]))