import pandas
from FileLoader import FileLoader

def proportionBySport(data, year, sport, gender):
    section = data.loc[(data["Year"] == year) & (data["Sex"] == gender)]
    section_sport = data.loc[(data["Year"] == year) & (data["Sex"] == gender) \
        & (data["Sport"] == sport)]
    return len(section_sport) / len(section)

def main():
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    print("")

    print(proportionBySport(data, 2004, 'Tennis', 'F'), end = "\n\n")
    # output is "0.02307"

    print(proportionBySport(data, 2008, 'Hockey', 'F'), end = "\n\n")
    # output is  "0.03284"

    print(proportionBySport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
    # output is "0.00659"

if __name__=="__main__":
    main()
