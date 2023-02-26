import pandas

def proportionBySport(data, year, sport, gender):
    section = data.loc[(data["Year"] == year) & (data["Sex"] == "F")]
    section_sport = data.loc[(data["Year"] == year) & (data["Sex"] == "F") \
        & (data["Sport"] == sport)]
    return len(section_sport) / len(section)