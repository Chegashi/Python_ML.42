def youngestfellah(data, year):
    data_f = data.loc[(data["Year"] == year) & (data["Sex"] == "F")]["Age"].min()
    data_m = data.loc[(data["Year"] == year) & (data["Sex"] == "M")]["Age"].min()
    return {'f': data_f, 'm': data_m}
