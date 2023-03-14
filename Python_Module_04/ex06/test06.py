from MyPlotLib import MyPlotLib
import pandas as pd
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader

features = ["Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"]

loader = FileLoader()
data = loader.load("../athlete_events.csv")
m = MyPlotLib()


m.density(data, ["Weight", "Height"])
m.histogram(data, ["Weight", "Height"])
m.pair_plot(data, ["Weight","Height"])
m.box_plot(data, ["Weight","Height"])