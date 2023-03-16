from FileLoader import FileLoader

def youngestfellah(data, year):
    data_f = data.loc[(data["Year"] == year) & (data["Sex"] == "F")]["Age"].min()
    data_m = data.loc[(data["Year"] == year) & (data["Sex"] == "M")]["Age"].min()
    return {'f': data_f, 'm': data_m}

def main():
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    print(youngestfellah(data, 1992))
    # output is: "{'f': 12.0, 'm': 11.0}"

    print(youngestfellah(data, 2004))
    # output is: "{'f': 13.0, 'm': 14.0}"

    print(youngestfellah(data, 2010))
    # output is: "{'f': 15.0, 'm': 15.0}"

    print(youngestfellah(data, 2003))
    # output is: "{'f': nan, 'm': nan}"

if __name__ == "__main__":
    main()
